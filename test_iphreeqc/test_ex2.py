"""
test_ex2.py, run examples/ex2 with iphreeqc.py

## USAGE
Try: 
    python -c "from test_iphreeqc.test_ex2 import ex2; print(ex2(lib=\"${HOME}/local/lib/iphreeqc-3.6.2-15100/libiphreeqc.so\", database=\"${HOME}/local/share/doc/iphreeqc-3.6.2-15100/database/phreeqc.dat\"))"

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
    test_ex2.py Copyright (C) 2020 Stuart Nolan

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

def ex2(lib="libiphreeqc.so", database="phreeqc.dat"):
    """
    Run file examples/ex2 from Phreeqc examples and use python to process
    selected output results

    Demonstrates:
        * RunFile(<FQPN>)
        * SetSelectedOutputStringOn()
        * GetSelectedOutputArray()
            - GetSelectedOutputRowCount()
            - GetSelectedOutputColumnCount()
            - GetSelectedOutputValue(<ridx>, <cidx>)

    See also "ex1_mod" found in iphreeqc.py

    Parameters:
        lib, FQPN to the iphreeqc shared library
        database, FQPN to the iphreeqc database "phreeqc.dat"  
    
    Return:
        ipcl, ex2 iphreeqc class instance.  For potential use in an 
              interactive python session

    Notes
     * Plots requested by the ex2 input file are not generated.  There is
       no indication regarding the (lack of) plots in the error, log, 
       output, or selected output strings.  Apparently, Phreeqc plotting 
       will fail silently if requested from iphreeqc.py under Linux. 

       GetSelectedOutputArray can be used to fetch selected output data 
       into a python list as originally demonstrated by Ravi Patel in 
       IPhreeqcPy.

       The selected output data can be inspected by using a python package 
       such as tabulate and the ex2 plots can be recreated by using a 
       python package such as matplotlib.  Note that using matplotlib in 
       place of Phreeqc's plotting functionality requires more effort  
       from the user in this case.
       
     * Error, output, and selected output string functionality is enabled.

     * To enable log and dump string output, the Phreeqc ex2 file would
       have to be modified by adding the lines:

           DUMP
             -all
           KNOBS
    	      -logfile

       See ex1_mod found in iphreeqc.py for a demonstration.
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
    ipcl.SetSelectedOutputStringOn()

    location = os.path.dirname(os.path.realpath(os.path.abspath(__file__)))
    runFile = os.path.join(location, 'examples', 'ex2')
    if os.path.isfile(runFile):
        ipcl.RunFile(runFile)
    else:
        print("File not found: %s" % runFile)
        return

    errorStr = ipcl.GetErrorString()
    outStr = ipcl.GetOutputString()
    selectedOutput = ipcl.GetSelectedOutputArray()
    
    print("\n\n*** Error String ***")
    print(errorStr) 

    print("\n\n*** Output String ***")
    print(outStr)

    print("\n\n*** Selected Output from GetSelectedOutputArray ***")
    try:
        from tabulate import tabulate
        header = selectedOutput[0]
        print(tabulate(selectedOutput[1:],headers=header))
    except ImportError as e:
        print("Python package tabulate is not installed.")
        print("Try: \"pip install tabulate\" to install it.")
        print(selectedOutput)

    ug1_ylabel="Saturation index"
    ug1_xlabel="Temperature, in degrees celsius"
    ug1_title="Gypsum-Anhydrite Stability"
    """
    By inspection of selectedOutput, saturation index vs temperature data 
    starts at row 2.  Temperature data is in column 8, anhydrite saturation 
    index data is in column 9, and gypsum saturation index data is in 
    column 10.
    """
    selOutByCol = list(zip(*selectedOutput[2:]))
    ug1_temp = selOutByCol[8]
    ug1_anhydriteSI = selOutByCol[9]
    ug1_gypsumSI = selOutByCol[10]

    try:
        import matplotlib.pyplot as plt
        print("Close the matplotlib plot window to continue...")
        plt.plot(ug1_temp,ug1_gypsumSI,'rs',label='Gypsum')
        plt.plot(ug1_temp,ug1_anhydriteSI,'gD',label='Anhydrite')
        plt.xlabel(ug1_xlabel)
        plt.ylabel(ug1_ylabel)
        plt.title(ug1_title)
        plt.axis([25, 75, -0.5, 0.01])
        plt.legend()
        plt.grid(linestyle='--')
        plt.show()
        
    except ImportError as e:
        print("Python package matplotlib is not installed.")
        print("Try: \"pip install matplotlib\" to install it.")
        print("Title: %s;\n x axis: %s;\n y axis: %s;" %
              (ug1_title, ug1_xlabel, ug1_ylabel))
        print("Gypsum si data: %s;\n Anhydrite si data: %s;" %
              (ug1_gypsumSI, ug1_anhydriteSI))

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

    ex2_ = ex2(lib, database)
