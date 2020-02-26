"""
test_ex5.py, run file examples/ex5

## USAGE
Try:
    python -c "from test_iphreeqc.test_ex5 import ex5; print(ex5(lib=\"${HOME}/local/lib/iphreeqc-3.6.2-15100/libiphreeqc.so\", database=\"${HOME}/local/share/doc/iphreeqc-3.6.2-15100/database/phreeqc.dat\"))"

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
    test_ex5.py Copyright (C) 2020 Stuart Nolan

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

def ex5(lib="libiphreeqc.so", database="phreeqc.dat"):
    """
    Run file examples/ex5 

    Demonstrates:
        * GetComponentList
          * GetComponentCount
          * GetComponent
        * GetComponent IndexError exception
        
    Parameters:
        lib, FQPN to the iphreeqc shared library
        database, FQPN to the iphreeqc database "phreeqc.dat"

    Return:
        ipcl, ex5 iphreeqc class instance.  For potential use in an 
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

    print("IPhreeqc shared library: %s" % ipcl.iPhreeqcLib)
    print("IPhreeqc database: %s" % ipcl.database)
    print("IPhreeqc version: %s" % ipcl.iPhreeqcLib_version)
    print("iphreeqc-py version: %s" % ipc.__version__)

    ipcl.SetOutputStringOn()

    location = os.path.dirname(os.path.realpath(os.path.abspath(__file__)))
    runFile = os.path.join(location, 'examples', 'ex5')
    if os.path.isfile(runFile):
        ipcl.RunFile(runFile)
    else:
        print("File not found: %s" % runFile)
        return

    outStr = ipcl.GetOutputString()

    print("\n\n*** Output String ***")
    print(outStr)

    print("*** Demo GetComponentList ***")
    print(ipcl.GetComponentList())
    try:
        ipcl.GetComponent(ipcl.GetComponentCount()+1)
    except IndexError as idxe:
        print("\n*** Test GetComponent IndexError exception  ***")
        print(idxe)

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

    ex5_ = ex5(lib, database)
