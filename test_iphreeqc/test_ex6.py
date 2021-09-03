"""
test_ex6.py, demo a modified version of examples/ex6

## USAGE
Try:
    python -c "from test_iphreeqc.test_ex6 import ex6; print(ex6(lib=\"${HOME}/local/lib/iphreeqc-3.7.1-15876/libiphreeqc.so\", database=\"${HOME}/local/share/doc/iphreeqc-3.7.1-15876/database/phreeqc.dat\"))"

## References & Attribution
    <https://www.usgs.gov/software/phreeqc-version-3>
        Note the files in the examples directory and content used from 
        these files elsewhere in iphreeqc-py are copied from:
    
        <http://water.usgs.gov/water-resources/software/PHREEQC/phreeqc-3.7.1-15876.tar.gz>
    
        and are distributed under the terms of the PHREEQC Public Domain
        declaration (see the "phreeqc-version-3" link above).

## License Notice
    SPDX-License-Identifier: LGPL-3.0-or-later
    Copyright (c) 2020 Stuart Nolan
"""
import os
import iphreeqc as ipc
__version__ = ipc.__version__

def ex6(lib="libiphreeqc.so", database="phreeqc.dat"):
    """
    Open and modify examples/ex6 

    Demonstrates:
        * ClearAccumulatedLines
        * DestroyIPhreeqc
        * OutputAccumulatedLines
        * SetDumpFileName
        * SetDumpFileOn
        * SetErrorFileName
        * SetErrorFileOn
        * SetLogFileName
        * SetLogFileOn
        * SetOutputFileName
        * SetOutputFileOn
        * SetSelectedOutputFileOn
        
    Parameters:
        lib, FQPN to the IPhreeqc shared library
        database, FQPN to the IPhreeqc database "phreeqc.dat"

    Return:
        ipcl, ex6 iphreeqc class instance.  For potential use in an 
              interactive python session
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

    ipcl.SetOutputFileOn()
    ipcl.SetOutputFileName("ex6.out")
    ipcl.SetSelectedOutputFileOn()
    # use selected output file name specified in ex6 input file
    ipcl.SetDumpFileOn()
    ipcl.SetDumpFileName("ex6.dmp")
    ipcl.SetLogFileOn()
    ipcl.SetLogFileName("ex6.log")
    ipcl.SetErrorFileOn()
    ipcl.SetErrorFileName("ex6.err")

    addLines = """DUMP
      -all
    KNOBS
      -logfile
    """
    addLines = addLines.splitlines()

    location = os.path.dirname(os.path.realpath(os.path.abspath(__file__)))
    runFile = os.path.join(location, 'examples', 'ex6')
    if os.path.isfile(runFile):
        runLines = open(runFile).read()
        runLines = runLines.splitlines()
        [runLines.insert(len(runLines)-1,item) for item in addLines]
        runLines = "\n".join(runLines)
        ipcl.AccumulateLine(runLines)
        ipcl.OutputAccumulatedLines()
        ipcl.RunAccumulated()        
    else:
        print("File not found: %s" % runFile)
        return

    print("IPhreeqc shared library: %s" % ipcl.IPhreeqcLib)
    print("IPhreeqc database: %s" % ipcl.database)
    print("IPhreeqc version: %s" % ipcl.IPhreeqcLib_version)
    print("iphreeqc-py version: %s" % ipc.__version__)

    return ipcl # for use in an interactive python session
        
if __name__ == '__main__':
    #
    # EDIT 'lib' to point to the IPhreeqc shared library location
    #
    install_prefix = os.path.join(os.getenv("HOME"), 'local')
    lib = os.path.join(install_prefix,
                       'lib',
                       'iphreeqc-3.7.1-15876',
                       'libiphreeqc.so')
    #
    # EDIT 'database' to point to the 'phreeqc.dat' location
    #
    database=os.path.join(install_prefix,
                          'share',
                          'doc',
                          'iphreeqc-3.7.1-15876',
                          'database',
                          'phreeqc.dat')

    ex6_ = ex6(lib, database)
