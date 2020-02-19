"""
iphreeqc.py a python 3+ ctypes wrapper for selected function prototypes 
defined by IPhreeqc version 3 in IPhreeqc.h and Var.h

Install & Usage: see https://github.com/stuart-nolan/iphreeqc-py 

Documentation: see IPhreeqc.h and Var.h

References & Attribution
    <https://www.usgs.gov/software/phreeqc-version-3>

    <https://www.phreeqpy.com/>
    PhreeqPy, Python Tools for PHREEQC
    Copyright 2011 Mike Mueller and contributors

    <http://raviapatel.bitbucket.io/IPhreeqcPy>
    IPhreeqcPy, a python wrapper for IPhreeqc
    Copyright 2016 Ravi Patel

This work is derived from IPhreeqcPy.

License Notice
    iphreeqc.py Copyright (C) 2020 Stuart Nolan

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Lesser General Public License as published 
    by the Free Software Foundation, version 3.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

License Usage Reference 
    <https://www.gnu.org/licenses/gpl-howto.html>

Notes
    #import tabulate
    #selOutput = ipcl.GetSelectedOutputArray()
    #header = selOutput[0]
    #print(tabulate(selOutput[1:],headers=header))
    runFile = os.path.join(install_prefix, 'src', 'python', 'example1.txt')
    #ipcl.RunFile(runFile)
"""
import ctypes
import os
__version__ = "0.1a1"
__revision_date__ = "2020.02.18"

class iphreeqc():
    def __init__(self, iPhreeqcLib):
        self.iPhreeqcLib=iPhreeqcLib
        ipcl = ctypes.cdll.LoadLibrary(self.iPhreeqcLib)
        
        methods = [('_AccumulateLine', ipcl.AccumulateLine,
                    [ctypes.c_int, ctypes.c_char_p], ctypes.c_int),
                   ('_AddError', ipcl.AddError,
                    [ctypes.c_int, ctypes.c_char_p], ctypes.c_int),
                   ('_AddWarning', ipcl.AddWarning,
                    [ctypes.c_int, ctypes.c_char_p], ctypes.c_int),
                   ('_ClearAccumulatedLines',
                    ipcl.ClearAccumulatedLines, [ctypes.c_int], ctypes.c_int),
                   ('_CreateIPhreeqc', ipcl.CreateIPhreeqc,
                    [ctypes.c_voidp], ctypes.c_int),
                   ('_DestroyIPhreeqc', ipcl.DestroyIPhreeqc,
                    [ctypes.c_int], ctypes.c_int),
                   ('_GetComponent', ipcl.GetComponent,
                    [ctypes.c_int, ctypes.c_int], ctypes.c_char_p),
                   ('_GetComponentCount', ipcl.GetComponentCount,
                    [ctypes.c_int], ctypes.c_int),
                   ('_GetCurrentSelectedOutputUserNumber',
                    ipcl.GetCurrentSelectedOutputUserNumber,
                    [ctypes.c_int], ctypes.c_int),
                   ('_GetDumpFileName', ipcl.GetDumpFileName,
                    [ctypes.c_int],  ctypes.c_char_p),
                   ('_GetDumpFileOn', ipcl.GetLogFileOn, [ctypes.c_int],
                    ctypes.c_int),
                   ('_GetDumpString', ipcl.GetDumpString, [ctypes.c_int],
                    ctypes.c_char_p),
                   ('_GetDumpStringLine', ipcl.GetDumpStringLine,
                    [ctypes.c_int, ctypes.c_int], ctypes.c_char_p),
                   ('_GetDumpStringLineCount', ipcl.GetErrorStringLineCount,
                    [ctypes.c_int], ctypes.c_int),
                   ('_GetDumpStringOn', ipcl.GetErrorFileOn, [ctypes.c_int],
                    ctypes.c_int),
                   ('_GetErrorFileName', ipcl.GetErrorFileName,
                    [ctypes.c_int],  ctypes.c_char_p),
                   ('_GetErrorFileOn', ipcl.GetErrorFileOn, [ctypes.c_int],
                    ctypes.c_int),
                   ('_GetErrorString', ipcl.GetErrorString, [ctypes.c_int],
                    ctypes.c_char_p),
                   ('_GetErrorStringLine', ipcl.GetErrorStringLine,
                    [ctypes.c_int, ctypes.c_int], ctypes.c_char_p),
                   ('_GetErrorStringLineCount', ipcl.GetErrorStringLineCount,
                    [ctypes.c_int], ctypes.c_int),
                   ('_GetErrorStringOn', ipcl.GetErrorStringOn,
                    [ctypes.c_int], ctypes.c_int),
                   ('_GetLogFileName', ipcl.GetLogFileName,
                    [ctypes.c_int],  ctypes.c_char_p),
                   ('_GetLogFileOn', ipcl.GetLogFileOn, [ctypes.c_int],
                    ctypes.c_int),
                   ('_GetLogString', ipcl.GetLogString,
                    [ctypes.c_int],  ctypes.c_char_p),
                   ('_GetLogStringLine', ipcl.GetLogStringLine,
                    [ctypes.c_int, ctypes.c_int], ctypes.c_char_p),
                   ('_GetLogStringLineCount', ipcl.GetLogStringLineCount,
                    [ctypes.c_int], ctypes.c_int),
                   ('_GetLogStringOn', ipcl.GetLogStringOn, [ctypes.c_int],
                    ctypes.c_int),
                   ('_GetOutputString', ipcl.GetOutputString,
                    [ctypes.c_int],  ctypes.c_char_p),
                   ('_GetOutputStringLine', ipcl.GetOutputStringLine,
                    [ctypes.c_int, ctypes.c_int], ctypes.c_char_p),
                   ('_GetOutputStringLineCount', ipcl.GetOutputStringLineCount,
                    [ctypes.c_int], ctypes.c_int),
                   ('_GetOutputStringOn', ipcl.GetOutputStringOn,
                    [ctypes.c_int], ctypes.c_int),
                   ('_GetSelectedOutputColumnCount',
                    ipcl.GetSelectedOutputColumnCount, [ctypes.c_int],
                    ctypes.c_int),
                   ('_GetSelectedOutputRowCount',
                    ipcl.GetSelectedOutputRowCount, [ctypes.c_int],
                    ctypes.c_int),
                   ('_GetSelectedOutputValue', ipcl.GetSelectedOutputValue,
                    [ctypes.c_int, ctypes.c_int, ctypes.c_int,
                     ctypes.POINTER(_VAR)], ctypes.c_int),
                   ('_GetVersionString', ipcl.GetVersionString,
                    [ctypes.c_voidp], ctypes.c_char_p),
                   ('_LoadDatabase', ipcl.LoadDatabase,
                    [ctypes.c_int, ctypes.c_char_p], ctypes.c_int),
                   ('_LoadDatabaseString', ipcl.LoadDatabaseString,
                    [ctypes.c_int, ctypes.c_char_p], ctypes.c_int),
                   ('_OutputAccumulatedLines', ipcl.OutputAccumulatedLines,
                    [ctypes.c_int], ctypes.c_voidp),
                   ('_RunAccumulated', ipcl.RunAccumulated,
                    [ctypes.c_int], ctypes.c_int),
                   ('_RunFile', ipcl.RunFile,
                    [ctypes.c_int, ctypes.c_char_p], ctypes.c_int),
                   ('_RunString', ipcl.RunString,
                    [ctypes.c_int, ctypes.c_char_p], ctypes.c_int),
                   ('_SetDumpFileName', ipcl.SetDumpFileName,
                    [ctypes.c_int, ctypes.c_char_p], ctypes.c_int),
                   ('_SetDumpFileOn', ipcl.SetDumpFileOn,
                    [ctypes.c_int,ctypes.c_int], ctypes.c_int),
                   ('_SetDumpStringOn', ipcl.SetDumpStringOn,
                    [ctypes.c_int,ctypes.c_int], ctypes.c_int),
                   ('_SetErrorFileName', ipcl.SetErrorFileName,
                    [ctypes.c_int, ctypes.c_char_p], ctypes.c_int),
                   ('_SetErrorFileOn', ipcl.SetErrorStringOn,
                    [ctypes.c_int,ctypes.c_int], ctypes.c_int),
                   ('_SetErrorStringOn', ipcl.SetErrorStringOn,
                    [ctypes.c_int,ctypes.c_int], ctypes.c_int),
                   ('_SetLogFileName', ipcl.SetLogFileName,
                    [ctypes.c_int, ctypes.c_char_p], ctypes.c_int),
                   ('_SetLogFileOn', ipcl.SetLogFileOn,
                    [ctypes.c_int, ctypes.c_int], ctypes.c_int),
                   ('_SetLogStringOn', ipcl.SetLogStringOn,
                    [ctypes.c_int, ctypes.c_int], ctypes.c_int),
                   ('_SetOutputFileName', ipcl.SetOutputFileName,
                    [ctypes.c_int, ctypes.c_char_p], ctypes.c_int),
                   ('_SetOutputFileOn', ipcl.SetOutputFileOn,
                    [ctypes.c_int, ctypes.c_int], ctypes.c_int),
                   ('_SetOutputStringOn', ipcl.SetOutputStringOn,
                    [ctypes.c_int, ctypes.c_int], ctypes.c_int),
                   ('_SetSelectedOutputFileName',
                    ipcl.SetSelectedOutputFileName,
                    [ctypes.c_int, ctypes.c_char_p], ctypes.c_int),
                   ('_SetSelectedOutputFileOn', ipcl.SetSelectedOutputFileOn,
                    [ctypes.c_int, ctypes.c_int], ctypes.c_int),
                   ('_SetSelectedOutputStringOn',
                    ipcl.SetSelectedOutputStringOn,
                    [ctypes.c_int, ctypes.c_int], ctypes.c_int)
        ]

        for name, obj, argtypes, restype in methods:
            obj.argtypes = argtypes
            obj.restype = restype
            setattr(self, name, obj)
        self.var = _VAR()
        self.phc_error_count = 0
        self.phc_warning_count = 0
        self.phc_database_error_count = 0
        self.id = self.CreateIPhreeqc()
        self.database = ""

    @staticmethod
    def _RaisePhreeqcError(error_code):
        """
        Parameters
            code, integer error code between -6 to 0 
        """
        error_codes = {0: 'Success (IPQ_OK)',
                       -1: 'Failure, Out of memory (IPQ_OUTOFMEMORY)',
                       -2: 'Failure, Invalid VAR type (IPQ_BADVARTYPE)',
                       -3: 'Failure, Invalid argument (IPQ_INVALIDARG)',
                       -4: 'Failure, Invalid row (IPQ_INVALIDROW)',
                       -5: 'Failure, Invalid column (IPQ_INVALIDCOL)',
                       -6: 'Failure, Invalid instance id (IPQ_BADINSTANCE)'}

        error = error_codes[error_code]
        if error:
            raise PhreeqcException(error)

    def _RaiseStringError(self, errors):
        """
        Raise an exception with message from IPhreeqc error.
        
        Parameters
        errors: integer
           Number of error occured
        
        """
        if errors > 1:
            msg = '%s errors occured.\n' % errors
        elif errors == 1:
            msg = 'An error occured.\n'
        else:
            msg = 'Wrong error number.'
        raise Exception(msg + self.GetErrorString())

    def AccumulateLine(self, line):
        errors = self._AccumulateLine(self.id, bytes(line, 'utf-8'))
        if errors != 0:
            self._RaiseStringError(errors)
    
    def AddError(self, phc_error_msg):
        """
        Appends the given error message and increments the error count.  
        Internally used fo create an error condition
        
        Parameters
        phc_error_msg: string
            Error message to append
        """
        errors = self._AddError(self.id, bytes(phc_error_msg, 'utf-8'))
        if errors < 0:
            self._RaiseStringError(errors)
        else:
            self.phc_error_count = errors

    def AddWarning(self, phc_warn_msg):
        """
        Appends the given warning message and increments the warning count.
        Internally used to create warning condition
        
        Parameters:
            phc_warn_msg, string warning massage to add
        """
        errors = self._AddWarning(self.id, bytes(phc_warn_msg, 'utf-8'))
        if errors < 0:
            self._RaiseStringError(errors)
        else:
            self.phc_warning_count = errors

    def ClearAccumulatedLines(self):
        errors = self._ClearAccumulatedLines(self.id)
        if errors != 0:
            self._RaiseStringError(errors)

    def CreateIPhreeqc(self):
        error_code = self._CreateIPhreeqc(ctypes.c_voidp())
        if error_code < 0:
            self._RaisePhreeqcError(error_code)
        id = error_code
        return id
        
    def DestroyIPhreeqc(self):
        error_code = self._DestroyIPhreeqc(self.id)
        if error_code < 0:
            self._RaisePhreeqcError(error_code)

    def GetComponent(self, index):
        """
        Parameters:
            index, zero-based integer index of the component
        """
        component = self._GetComponent(self.id, index).decode('utf-8')
        if not component:
            raise IndexError('No component for index %s' % index)
        return component

    def GetComponentCount(self):
        return self._GetComponentCount(self.id)

    def GetComponentList(self):
        """
        Returns:
            list of all component names
        """
        return [self.GetComponent(index) for index in
                range(self.GetComponentCount())]

    def GetCurrentSelectedOutputUserNumber(self):
        return self._GetCurrentSelectedOutputUserNumber(self.id)

    def GetDumpFileName(self):
        return self._GetDumpFileName(self.id).decode('utf-8')
 
    def GetDumpFileOn(self):
        return self._GetDumpFileOn(self.id)
 
    def GetDumpString(self):
        return self._GetDumpString(self.id).decode('utf-8')
 
    def GetDumpStringLine(self, lidx):
        """
        Parameters:
            lidx, integer line index (can be negative to index back from the 
                  end of string)
        
        Returns:
            one line from dump string at line lidx        
        """
        if lidx < 0:
            lidx = self.GetDumpStringLineCount() + lidx
        return self._GetDumpStringLine(self.id,
                                      lidx).decode('utf-8', errors='ignore')
 
    def GetDumpStringLineCount(self):
        return self._GetDumpStringLineCount(self.id)
 
    def GetDumpStringOn(self):
        return self._GetDumpStringOn(self.id)
 
    def GetErrorFileName(self):
        return self._GetErrorFileName(self.id).decode('utf-8')
 
    def GetErrorFileOn(self):
        return self._GetErrorFileOn(self.id)
 
    def GetErrorString(self):
        return self._GetErrorString(self.id).decode('utf-8')

    def GetErrorStringLine(self, lidx):
        """
        Parameters:
            lidx, integer line index (can be negative to index back from the 
                  end of string)
        
        Returns:
            one line from error string at line lidx        
        """
        if lidx < 0:
            lidx = self.GetErrorStringLineCount() + lidx
        return self._GetErrorStringLine(self.id,
                                      lidx).decode('utf-8', errors='ignore')
 
    def GetErrorStringLineCount(self):
        return self._GetErrorStringLineCount(self.id)
 
    def GetErrorStringOn(self):
        return self._GetErrorStringOn(self.id)

    def GetLogFileName(self):
        return self._GetLogFileName(self.id).decode('utf-8')
 
    def GetLogFileOn(self):
        return self._GetLogFileOn(self.id)
 
    def GetLogString(self):
        return self._GetLogString(self.id).decode('utf-8')
 
    def GetLogStringLine(self, lidx):
        """
        Parameters:
            lidx, integer line index (can be negative to index back from the 
                  end of string)
        
        Returns:
            one line from log string at line lidx        
        """
        if lidx < 0:
            lidx = self.GetLogStringLineCount() + lidx
        return self._GetLogStringLine(self.id,
                                      lidx).decode('utf-8', errors='ignore')
 
    def GetLogStringLineCount(self):
        return self._GetLogStringLineCount(self.id)
 
    def GetLogStringOn(self):
        return self._GetLogStringOn(self.id)
 
    def GetOutputString(self):
        return self._GetOutputString(self.id).decode('utf-8',errors='ignore')
 
    def GetOutputStringLine(self, lidx):
        """
        Parameters:
            lidx, integer line index (can be negative to index back from the 
                  end of string)
        
        Returns:
            one line from output string at line lidx        
        """
        if lidx < 0:
            lidx = self.GetOutputStringLineCount() + lidx
        return self._GetOutputStringLine(self.id,
                                         lidx).decode('utf-8', errors='ignore')
 
    def GetOutputStringLineCount(self):
        return self._GetOutputStringLineCount(self.id)
 
    def GetOutputStringOn(self):
        return self._GetOutputStringOn(self.id)
 
    def GetSelectedOutputArray(self):
        """
        Get all values from the selected output
        
        Returns:
            rows, list of list of rows from the selected output
        """
        rows = []
        for ridx in range(self.GetSelectedOutputRowCount()):
            row = []
            for cidx in range(self.GetSelectedOutputColumnCount()):
                row.append(self.GetSelectedOutputValue(ridx, cidx))
            rows.append(row)
        return rows

    def GetSelectedOutputCol(self, cidx):
        """
        Return one column (all rows) from selected output at column index cidx

        Parameters:
            cidx, integer column index (can be negative to index back from the 
                  end)
        
        Returns:
            col, list of all rows from selected output at cidx
        """
        if cidx < 0:
            cidx = self.GetSelectedOutputColumnCount() + cidx
        col = []
        for ridx in range(self.GetSelectedOutputRowCount()):
            col.append(self.GetSelectedOutputValue(ridx, cidx))
        return col

    def GetSelectedOutputColumnCount(self):
        return self._GetSelectedOutputColumnCount(self.id)

    def GetSelectedOutputRow(self, ridx):
        """
        Return one row (all columns) from selected output at row index ridx

        Parameters:
            ridx, integer row index (can be negative to index back from the end
                  end)
        
        Returns:
            row, list of all columns from selected output at ridx
        """
        if ridx < 0:
            ridx = self.GetSelectedOutputRowCount() + ridx
        row = []
        for cidx in range(self.GetSelectedOutputColumnCount()):
            row.append(self.GetSelectedOutputValue(ridx, cidx))
        return row

    def GetSelectedOutputRowCount(self):
        return self._GetSelectedOutputRowCount(self.id)

    def GetSelectedOutputValue(self, ridx, cidx):
        """
        Parameters:
            ridx, integer row index
            cidx, integer column index
        
        Returns:
            val, one selected output value at ridx and cidx
        """
        error_code = self._GetSelectedOutputValue(self.id, ridx, cidx, self.var)
        if error_code != 0:
            self._RaisePhreeqcError(error_code)
        if self.var.type_ == 3:
            val = self.var.value.double_value
        elif self.var.type == 2:
            val = self.var.value.long_value
        elif self.var.type == 4:
            val = self.var.value.string_value.decode('utf-8')
        elif self.var.type == 0:
            val = None
        if self.var.type == 1:
            self.raise_error(value.error_code)
        return val

    def GetVersionString(self):
        return self._GetVersionString(self.id).decode('utf-8')

    def LoadDatabase(self, database):
        """
        Usage: see example below

        Parameters:
            database, fully qualified path name string to the iphreeqc
                      database to load.  E.g.,
                      "/<iphreeqc library install PREFIX>
                       /share/doc/iphreeqc/database/phreeqc.dat"
        """
        self.database=database
        self.phc_database_error_count = self._LoadDatabase(
            self.id, bytes(self.database, 'utf-8'))

    def LoadDatabaseString(self, input_string):
        self.phc_database_error_count = self._LoadDatabaseString(
            self.id, ctypes.c_char_p(bytes(input_string, 'utf-8')))

    def OutputAccumulatedLines(self):
        """
        output accumulated lines to stdout (i.e. not inside python)
        """
        self._OutputAccumulatedLines(self.id)
    
    def RunAccumulated(self):
        """
        """
        errors = self._RunAccumulated(self.id)
        if errors != 0:
            self._RaiseStringError(errors)
    
    def RunFile(self,runFQPN):
        """
        Parameters:
            runFQPN, fully qualified path name string to a "run" file 
            containing valid phreeqc instructions
        """
        errors = self._RunFile(self.id, bytes(runFQPN, 'utf-8'))
        if errors != 0:
            self._RaiseStringError(errors)
            
    def RunString(self, cmd_string):
        """
        Parameters:
            cmd_string, phreeqc command string to be executed
        """
        errors = self._RunString(self.id,
                                  ctypes.c_char_p(bytes(cmd_string, 'utf-8')))
        if errors != 0:
            self._RaiseStringError(errors)
    
    def SetDumpFileName(self,dmpFQPN):
        """
        Parameters:
            dmpFQPN, fully qualified path name string to a dump file
        """
        errors = self._SetDumpFileName(self.id,  bytes(dmpFQPN, 'utf-8'))
        if errors != 0:
            self._RaiseStringError(errors)
            
    def SetDumpFileOn(self,val=1):
        """
        Parameters:
            val, 0 = OFF; 1 = ON
        """
        errors = self._SetDumpFileOn(self.id,val)
        if errors != 0:
            self._RaiseStringError(errors)

    def SetDumpStringOn(self,val=1):
        """
        Parameters:
            val, 0 = OFF; 1 = ON
        """
        errors = self._SetDumpStringOn(self.id,val)
        if errors != 0:
            self._RaiseStringError(errors)

    def SetErrorFileName(self,errFQPN):
        """
        Parameters:
            errFQPN, fully qualified path name string to an error file
        """
        errors = self._SetErrorFileName(self.id,  bytes(errFQPN, 'utf-8'))
        if errors != 0:
            self._RaiseStringError(errors)
            
    def SetErrorFileOn(self,val=1):
        """
        Parameters:
            val, 0 = OFF; 1 = ON
        """
        errors = self._SetErrorFileOn(self.id,val)
        if errors != 0:
            self._RaiseStringError(errors)

    def SetErrorStringOn(self,val=1):
        """
        Parameters:
            val, 0 = OFF; 1 = ON
        """
        errors = self._SetErrorStringOn(self.id,val)
        if errors != 0:
            self._RaiseStringError(errors)

    def SetLogFileName(self,logFQPN):
        """
        Parameters:
            logFQPN, fully qualified path name string to a log file
        """
        errors = self._SetLogFileName(self.id,  bytes(logFQPN, 'utf-8'))
        if errors != 0:
            self._RaiseStringError(errors)
            
    def SetLogFileOn(self,val=1):
        """
        Parameters:
            val, 0 = OFF; 1 = ON
        """
        errors = self._SetLogFileOn(self.id,val)
        if errors != 0:
            self._RaiseStringError(errors)

    def SetLogStringOn(self,val=1):
        """
        Parameters:
            val, 0 = OFF; 1 = ON
        """
        errors = self._SetLogStringOn(self.id,val)
        if errors != 0:
            self._RaiseStringError(errors)

    def SetOutputFileOn(self,val=1):
        """
        Parameters:
            val, 0 = OFF; 1 = ON
        """
        errors = self._SetOutputFileOn(self.id,val)
        if errors != 0:
            self._RaiseStringError(errors)

    def SetOutputStringOn(self,val=1):
        """
        Parameters:
            val, 0 = OFF, 1 = ON
        """
        errors = self._SetOutputStringOn(self.id,val)
        if errors != 0:
            self._RaiseStringError(errors)

    def SetSelectedOutputFileName(self,soutFQPN):
        """
        Parameters:
            soutFQPN, fully qualified path name string to a selected output file
        """
        errors = self._SetSelectedOutputFileName(self.id,
                                                 bytes(soutFQPN, 'utf-8'))
        if errors != 0:
            self._RaiseStringError(errors)
            
    def SetSelectedOutputFileOn(self,val=1):
        """
        Parameters:
            val, 0 = OFF; 1 = ON
        """
        errors = self._SetSelectedOutputFileOn(self.id, val)
        if errors != 0:
            self._RaiseStringError(errors)
            

    def SetSelectedOutputStringOn(self,val=1):
        """
        Parameters:
            val, 0 = OFF; 1 = ON
        """
        errors = self._SetSelectedOutputStringOn(self.id, val)
        if errors != 0:
            self._RaiseStringError(errors)
            

class _VARUNION(ctypes.Union):
    # pylint: disable-msg=R0903
    # no methods
    """Union with types.

    See Var.h in PHREEQC source.
    """
    _fields_ = [('long_value', ctypes.c_long),
                ('double_value', ctypes.c_double),
                ('string_value', ctypes.c_char_p),
                ('error_code', ctypes.c_int)]

class _VAR(ctypes.Structure):
    # pylint: disable-msg=R0903
    # no methods
    """Struct with data type and data values.

    See Var.h in PHREEQC source.
    """
    _fields_ = [('type', ctypes.c_int),
                ('value', _VARUNION)]

class PhreeqcException(Exception):
    """Error in Phreeqc call.
    """
    pass

def example1(lib="libiphreeqc.so", database="phreeqc.dat"):
    if os.path.isfile(lib):
        ipcl=iphreeqc(lib)
    else:
        print("IPhreeqc library not found: %s" % lib)
        quit()

    if os.path.isfile(database):
        ipcl.LoadDatabase(database)
    else:
        print("database phreeqc.dat not found: %s" % database)
        quit()

    print("Using iphreeqc library: %s" % ipcl.iPhreeqcLib)
    print("Using iphreeqc version: %s" % ipcl.GetVersionString())
    print("Using database: %s" % ipcl.database)
    
    ipcl.SetDumpStringOn()
    ipcl.SetErrorStringOn()
    ipcl.SetLogStringOn()
    ipcl.SetOutputStringOn()
    
    ipcl.AccumulateLine(
    """
    TITLE Example 1. Add uranium and speciate seawater.
    SOLUTION 1 SEAWATER FROM NORDSTROM AND OTHERS (1979)
      units ppm
      pH 8.22
      pe 8.451
      density 1.023
      temp 25.0
      redox O(0)/O(-2)
      Ca 412.3
      Mg 1291.8
      Na 10768.0
      K 399.1
      Fe 0.002
      Mn 0.0002 pe
      Si 4.28
      Cl 19353.0
      Alkalinity 141.682 as HCO3
      S(6) 2712.0
      N(5) 0.29 gfw 62.0
      N(-3) 0.03 as NH4
      U 3.3 ppb N(5)/N(-3)
      O(0) 1.0 O2(g) -0.7
    SOLUTION_MASTER_SPECIES
      U U+4 0.0 238.0290 238.0290
      U(4) U+4 0.0 238.0290 
      U(5) UO2+ 0.0 238.0290
      U(6) UO2+2 0.0 238.0290
    SOLUTION_SPECIES
      # primary master species for U
      # is also secondary master species for U(4)
      U+4 = U+4
      log_k 0.0
    SOLUTION_SPECIES
      U+4 + 4 H2O = U(OH)4 + 4 H+
        log_k -8.538
        delta_h 24.760 kcal
      U+4 + 5 H2O = U(OH)5- + 5 H+
        log_k -13.147
        delta_h 27.580 kcal
      # secondary master species for U(5)
      U+4 + 2 H2O = UO2+ + 4 H+ + e-
        log_k -6.432
        delta_h 31.130 kcal
      # secondary master species for U(6)
      U+4 + 2 H2O = UO2+2 + 4 H+ + 2 e-
        log_k -9.217
        delta_h 34.430 kcal
      UO2+2 + H2O = UO2OH+ + H+
        log_k -5.782 
        delta_h 11.015 kcal
      2UO2+2 + 2H2O = (UO2)2(OH)2+2 + 2H+
        log_k -5.626
        delta_h -36.04 kcal
      3UO2+2 + 5H2O = (UO2)3(OH)5+ + 5H+
        log_k -15.641
        delta_h -44.27 kcal
      UO2+2 + CO3-2 = UO2CO3
        log_k 10.064
        delta_h 0.84 kcal
      UO2+2 + 2CO3-2 = UO2(CO3)2-2
        log_k 16.977
        delta_h 3.48 kcal
      UO2+2 + 3CO3-2 = UO2(CO3)3-4
        log_k 21.397
        delta_h -8.78 kcal
    PHASES
      Uraninite
        UO2 + 4 H+ = U+4 + 2 H2O
          log_k -3.490
          delta_h -18.630 kcal
    DUMP
      -all
    KNOBS
      -logfile
    END
    """)

    ipcl.RunAccumulated()
    
    print("\n\n*** Output String ***")
    outStr = ipcl.GetOutputString()
    print(outStr)

    print("\n\n*** Dump String ***")
    dmpStr = ipcl.GetDumpString()
    print(dmpStr) 

    print("\n\n*** Error String ***")
    errStr = ipcl.GetErrorString()
    print(errStr) 

    print("\n\n*** Log String ***\n\n")
    logStr = ipcl.GetLogString()
    print(logStr)
    
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

    example1(lib,database)
