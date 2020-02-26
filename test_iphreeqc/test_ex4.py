"""
test_ex4.py, run file examples/ex4 and test error handling in iphreeqc.py

## USAGE
Try:
    python -c "from test_iphreeqc.test_ex4 import ex4_err; print(ex4_err(lib=\"${HOME}/local/lib/iphreeqc-3.6.2-15100/libiphreeqc.so\", database=\"${HOME}/local/share/doc/iphreeqc-3.6.2-15100/database/phreeqc.dat\"))"

## References & Attribution
    <https://www.usgs.gov/software/phreeqc-version-3>
        Note the files in the examples directory and content used from 
        these files elsewhere in iphreeqc-py are copied from:
    
        <http://water.usgs.gov/water-resources/software/PHREEQC/phreeqc-3.6.2-15100.tar.gz>
    
        and are distributed under the terms of the PHREEQC Public Domain
        declaration (see the "phreeqc-version-3" link above).

    <http://raviapatel.bitbucket.io/IPhreeqcPy>
    IPhreeqcPy, a python wrapper for IPhreeqc
    Copyright 2016 Ravi Patel

    <https://github.com/stuart-nolan/iphreeqc-py>
    iphreeqc-py Copyright (C) 2020 Stuart Nolan

## License Notice
    test_ex4.py Copyright (C) 2020 Stuart Nolan

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Lesser General Public License as
    published by the Free Software Foundation, version 3.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
import os
import iphreeqc as ipc
__version__ = ipc.__version__

def ex4_err(lib="libiphreeqc.so", database="phreeqc.dat"):
    """
    Run file examples/ex4 and then demo iphreeqc error handling

    Demonstrates:
        * _RaiseIPhreeqcError
        * AddError
        * AddWarning
        * IPhreeqcError
        * GetErrorStringLine
        * GetErrorStringLineCount
        * GetLogStringLine
        * GetLogStringLineCount
        * GetWarningString
        * GetWarningStringLine
        * GetWarningStringLineCount
        * RunString
        
    Parameters:
        lib, FQPN to the iphreeqc shared library
        database, FQPN to the iphreeqc database "phreeqc.dat"

    Return:
        ipcl, ex4_err iphreeqc class instance.  For potential use in an 
              interactive python session

    Notes:
    """
    if os.path.isfile(lib):
        ipcl=ipc.iphreeqc(lib)
    else:
        print("IPhreeqc library not found: %s" % lib)
        return

    if os.path.isfile(database):
        ipcl.LoadDatabase(database)
    else:
        print("database phreeqc.dat not found: %s" % database)
        return

    print("IPhreeqc shared library: %s" % ipcl.iPhreeqcLib)
    print("IPhreeqc database: %s" % ipcl.database)
    print("IPhreeqc version: %s" % ipcl.iPhreeqcLib_version)
    print("iphreeqc-py version: %s" % ipc.__version__)

    ipcl.SetErrorStringOn()
    ipcl.SetOutputStringOn()

    location = os.path.dirname(os.path.realpath(os.path.abspath(__file__)))
    runFile = os.path.join(location, 'examples', 'ex4')
    if os.path.isfile(runFile):
        ipcl.RunFile(runFile)
    else:
        print("File not found: %s" % runFile)
        return

    outStr = ipcl.GetOutputString()

    print("\n\n*** Output String ***")
    print(outStr)

    ipcl.SetLogStringOn()
    enableLogCmd="KNOBS\n-logfile\nEND"
    ipcl.RunString(enableLogCmd)

    eCount = ipcl.AddError("*** Intentionally generated errors below ***")
    print(ipcl.GetErrorString())

    try:
        ipcl.RunFile('path/to/invalid/file')
    except ipc.IPhreeqcError as ipce:
        print(ipce)
    
    try:
        ipcl.LoadDatabase('path/to/invalid/database')
    except ipc.IPhreeqcError as ipce:
        print(ipce)
        
    errorMsg = "iphreeqc-py error code: 2 and message: ALARM!!!"
    for code in range(-6,3):
        try:
            print("\nTrying error code: %s:" % code)
            ipcl._RaiseIPhreeqcError(code,error=errorMsg)
        except ipc.IPhreeqcError as ipce:
            print("\n*** IPhreeqcError Output ***")
            print(ipce)

    print("\n*** Error String ***")
    print(ipcl.GetErrorString())
    print("GetErrorStringLineCount: %s" % ipcl.GetErrorStringLineCount())

    eCount = ipcl.AddError("ADD ERROR 1")
    print("\n*** Error String ***")
    print(ipcl.GetErrorString())
    print("GetErrorStringLineCount: %s" % ipcl.GetErrorStringLineCount())
    print("Error Count: %s" % eCount)

    eCount = ipcl.AddError("\nADD ERROR 2")
    print("\n*** Error String ***")
    print(ipcl.GetErrorString())
    print("GetErrorStringLineCount: %s" % ipcl.GetErrorStringLineCount())
    print("Error Count: %s" % eCount)
    
    print("\n*** Error String via GetErrorStringLine(<line index>) ***")
    for lidx in range(0,eCount):
        print("Error String Line %s: %s" % (lidx,
                                            ipcl.GetErrorStringLine(lidx)))    
    print("\n*** Warning String ***")
    print(ipcl.GetWarningString())
    print("GetWarningStringLineCount: %s" % ipcl.GetWarningStringLineCount())

    wCount = ipcl.AddWarning("ADD WARNING 1\n")
    print("\n*** Warning String ***")
    print(ipcl.GetWarningString())
    print("GetWarningStringLineCount: %s" % ipcl.GetWarningStringLineCount())
    print("Warning Count: %s" % wCount)

    wCount = ipcl.AddWarning("ADD WARNING 2\n")
    print("\n*** Warning String ***")
    print(ipcl.GetWarningString())
    print("GetWarningStringLineCount: %s" % ipcl.GetWarningStringLineCount())
    print("Warning Count: %s" % wCount)
    
    print("\n*** Warning String via GetWarningStringLine(<line index>) ***")
    for lidx in range(0,wCount):
        print("Warning String Line %s: %s" % (lidx,
                                              ipcl.GetWarningStringLine(lidx)))    
    print("\n*** Log String ***")
    logStr = ipcl.GetLogString() 
    print(logStr)
    print("GetLogStringLineCount: %s" % ipcl.GetLogStringLineCount())
    print("Number of lines returned by GetLogString: %s" %
          logStr.count('\n'))
    print("\n*** Log String via GetLogStringLine(<line index>) ***")
    for lidx in range(0,logStr.count('\n')):
        print("Log String Line %s: %s" % (lidx,
                                          ipcl.GetLogStringLine(lidx))) 
    print("""

    Error, log, and warning string behaviour notes:
     * the error string buffer is cleared when a new error is generated
       by an iphreeqc shared library method, except:
       - the error string buffer is retained between succusive calls to
         AddError
     * AddError returns the "error count" but does not increment
       the the value returned by GetErrorStringLineCount
     * GetErrorStringLine(<line index>) will not return error string
       buffer lines added by AddError
     * AddWarning, GetWarningStringLineCount, and 
       GetWarningStringLine(<line index>) behave the same as their error
       counterparts
     * the log string buffer retains errors generated by iphreeqc
       shared library methods but,
     * the methods AddError and AddWarning only add messages to their 
       respective string buffers, *not the log string buffer.*
     * error strings captured in the log string buffer do not increment
       the value returned by GetLogStringLineCount

     Who knew.

    """)

    return ipcl # for use in an interactive python session
        
if __name__ == '__main__':
    #
    # EDIT 'lib' to point to the iphreeqc shared library location
    #
    install_prefix = os.path.join(os.getenv("HOME"), 'local')
    lib = os.path.join(install_prefix,
                       'lib',
                       'iphreeqc-3.6.2-15100',
                       'libiphreeqc.so')
    #
    # EDIT 'database' to point to the 'phreeqc.dat' location
    #
    database=os.path.join(install_prefix,
                          'share',
                          'doc',
                          'iphreeqc-3.6.2-15100',
                          'database',
                          'phreeqc.dat')

    ex4_err_ = ex4_err(lib, database)
