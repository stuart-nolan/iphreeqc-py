"""
test_ex3.py, run examples/ex3 with iphreeqc.py

## USAGE
Try: 
    python -c "from test_iphreeqc.test_ex3 import ex3; print(ex3(lib=\"${HOME}/local/lib/iphreeqc-3.6.2-15100/libiphreeqc.so\", database=\"${HOME}/local/share/doc/iphreeqc-3.6.2-15100/database/phreeqc.dat\"))"

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
    test_ex3.py Copyright (C) 2020 Stuart Nolan

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

def ex3(lib="libiphreeqc.so", database="phreeqc.dat"):
    """
    Run file examples/ex3 from Phreeqc examples and print output
    string

    Parameters:
        lib, FQPN to the iphreeqc shared library
        database, FQPN to the iphreeqc database "phreeqc.dat"

    Return:
        ipcl, ex3 iphreeqc class instance.  For potential use in an 
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
    print("IPhreeqc version: %s" % ipcl.iPhreeqcLib_version)
    print("iphreeqc-py version: %s" % ipc.__version__)

    ipcl.SetErrorStringOn()
    ipcl.SetOutputStringOn()

    location = os.path.dirname(os.path.realpath(os.path.abspath(__file__)))
    runFile = os.path.join(location, 'examples', 'ex3')
    if os.path.isfile(runFile):
        ipcl.RunFile(runFile)
    else:
        print("File not found: %s" % runFile)
        return

    errorStr = ipcl.GetErrorString()
    outStr = ipcl.GetOutputString()
    
    print("\n\n*** Error String ***")
    print(errorStr) 

    print("\n\n*** Output String ***")
    print(outStr)

    return ipcl # for use in an interactive python session

def ex3_mod(lib="libiphreeqc.so", database="phreeqc.dat"):
    """
    ex3 modified, a "selected_ouput [<user number index>]" learning 
                  exercise

    Demonstrates:
        GetCurrentSelectedOutputUserNumber()
        GetNthSelectedOutputUserNumber(<index>)
        GetSelectedOutputCount()
        SetCurrentSelectedOutputUserNumber(<index>)

    Parameters:
        lib, FQPN to the iphreeqc shared library
        database, FQPN to the iphreeqc database "phreeqc.dat"  
    
    Return:
        ipcl, ex3_mod iphreeqc class instance.  For potential use in an
              interactive python session

    Notes:
    * See the iphreeqc-3.6.2-15100 html documentation on
      SetCurrentSelectedOutputUserNumber.  In particular, under 
      "C Example:" see the listing of "File multi_punch" for an
      example using user numbers with Selected_Output.

    * Selected_Output [<user number index>] behavior:
      - all selected output is accumulated from the point a user number
        index is first used until a block like the following is used:

            SELECTED_OUTPUT [<prior user number index>]
                -active false
            END

        *even if new user number indexes are used*

        i.e. without "-active false" for any defined user number index, 
        subsequent selected_output [<new user number index>] blocks will
        contain data from prior selected_output [<prior user number index>] 
        blocks until <prior user number index> is made inactive

      - the default selected output columns for user number index 1 are not
        preserved for subsequent user number indexes (i.e. subsequent 
        selected_output [<new user number index>] blocks default to 
        "-reset false"?)

      - the selected output buffer is not preserved between calls to 
        RunAccumulated and/or RunString
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
    print("IPhreeqc version: %s" % ipcl.iPhreeqcLib_version)
    print("iphreeqc-py version: %s" % ipc.__version__)

    ipcl.SetLogStringOn()
    ipcl.SetErrorStringOn()
    ipcl.SetOutputStringOn()
    ipcl.SetSelectedOutputStringOn()
    ipcl.AccumulateLine(
"""
TITLE Example 3, part A.--Calcite equilibrium at log Pco2 = -2.0 and 25C.        
SOLUTION 1  Pure water
        pH      7.0
        temp    25.0
EQUILIBRIUM_PHASES
        CO2(g)          -2.0    
        Calcite         0.0
SELECTED_OUTPUT 1
        -distance false
        -e calcite dolomite
        -p co2(g)
        -pe false
        -pH true
        -si co2(g) calcite dolomite
        -simulation true
        -solution false
        -state true
        -step false
        -time false
SAVE solution 1
KNOBS
	-logfile
END
SELECTED_OUTPUT 1
        -active false
END
TITLE Example 3, part B.--Definition of seawater.
SOLUTION 2  Seawater
        units   ppm
        pH      8.22
        pe      8.451
        density 1.023
        temp    25.0
        Ca              412.3
        Mg              1291.8
        Na              10768.0
        K               399.1
        Si              4.28
        Cl              19353.0
        Alkalinity      141.682 as HCO3
        S(6)            2712.0
SELECTED_OUTPUT 2
        -e calcite dolomite
        -p co2(g)
        -pH true
        -simulation true
        -si co2(g) calcite  dolomite
        -state true
END
SELECTED_OUTPUT 2
        -active false
END
TITLE Example 3, part C.--Mix 70% groundwater, 30% seawater.
MIX 1
        1      0.7
        2      0.3
SELECTED_OUTPUT 3
        -e calcite dolomite
        -p co2(g)
        -pH true
        -simulation true
        -si co2(g) calcite  dolomite
        -state true
SAVE solution   3
END
SELECTED_OUTPUT 3
        -active false
END
TITLE Example 3, part D.--Equilibrate mixture with calcite and dolomite.
EQUILIBRIUM_PHASES 1
        Calcite         0.0
        Dolomite        0.0
USE solution 3
SELECTED_OUTPUT 4
        -e calcite dolomite
        -p co2(g)
        -pH true
        -simulation true
        -si co2(g) calcite  dolomite
        -state true
END
SELECTED_OUTPUT 4
        -active false
END
TITLE Example 3, part E.--Equilibrate mixture with calcite only.
EQUILIBRIUM_PHASES 2
        Calcite         0.0
USE solution 3
SELECTED_OUTPUT 5
        -e calcite dolomite
        -p co2(g)
        -pH true
        -simulation true
        -si co2(g) calcite  dolomite
        -state true
END
SELECTED_OUTPUT 5
        -active false
END
"""
    )
    ipcl.RunAccumulated()

    logStr = ipcl.GetLogString()
    errorStr = ipcl.GetErrorString()
    outStr = ipcl.GetOutputString()
    
    print("\n\n*** Log String ***")
    print(logStr) 

    print("\n\n*** Error String ***")
    print(errorStr) 

    print("\n\n*** Output String ***")
    print(outStr)

    print("\n\n*** Reproduce Table 16 ***")
    # header for Table 16. Selected results for example 3.
    header = ["Simulation","pH","log P_CO2", "SI Calcite", "SI Dolomite",
              "CO2 trans. /mol", "Calcite trans. /mol",
              "Dolomite trans. /mol"]
    translate = {"pH": "pH",
                 "si_co2(g)": "log P_CO2",
                 "si_dolomite": "SI Dolomite",
                 "si_calcite": "SI Calcite",
                 "d_calcite": "Calcite trans. /mol",
                 'd_co2(g)': "CO2 trans. /mol",
                 "d_dolomite": "Dolomite trans. /mol"}
                 
    # initialize a list of lists for Table 16.
    table = [["A","","","","--","","","--"],
             ["B","","","","","--","--","--"],
             ["C","","","","","--","--","--"],
             ["D","","","","","--","",""],
             ["E","","","","","--","","--"]]
    
    for idx in range(0,ipcl.GetSelectedOutputCount()):
        sOidx = ipcl.GetNthSelectedOutputUserNumber(idx)
        ipcl.SetCurrentSelectedOutputUserNumber(sOidx)
        print("Populating table with data from user number %s" %
              ipcl.GetCurrentSelectedOutputUserNumber())
        selOut = ipcl.GetSelectedOutputArray()
        table2SO_jdx = {}
        for jdx,item in enumerate(selOut[0]):
            if item in translate:
                if translate[item] in header:
                    table_jdx=header.index(translate[item])
                if table[idx][table_jdx] == "":
                    # the desired data from selOut is always the last list
                    table[idx][table_jdx] = selOut[len(selOut)-1][jdx]
    
    try:
        from tabulate import tabulate
        print("\n",tabulate(table,headers=header))
    except ImportError as e:
        print("Python package tabulate is not installed.")
        print("Try: \"pip install tabulate\" to install it.")
        print(header,table)

    print("\nIt can be done.  Should it be done this way?")

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

    ex3_ = ex3(lib, database)
    ex3_mod_ = ex3_mod(lib, database)
