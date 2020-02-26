"""
A python 3+ ctypes wrapper for selected function prototypes 
defined by IPhreeqc version 3 in IPhreeqc.h and Var.h

Install & Usage: see https://github.com/stuart-nolan/iphreeqc-py 

Documentation: see IPhreeqc.h and Var.h

References & Attribution
    <https://www.usgs.gov/software/phreeqc-version-3>
        Note the files in the examples directory and content used from 
        these files elsewhere in iphreeqc-py are copied from:
    
        <http://water.usgs.gov/water-resources/software/PHREEQC/phreeqc-3.6.2-15100.tar.gz>
    
        and are distributed under the terms of the PHREEQC Public Domain
        declaration (see the "phreeqc-version-3" link above).

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
    it under the terms of the GNU Lesser General Public License as
    published by the Free Software Foundation, version 3.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

License Usage Reference 
    <https://www.gnu.org/licenses/gpl-howto.html>
"""
import ctypes
import os
__version__ = "0.1a5"

class iphreeqc():
    def __init__(self, iPhreeqcLib):
        self.iPhreeqcLib=iPhreeqcLib

        self.errors = {0: 'Success (IPQ_OK)',
                       1: 'Error string',
                       -1: 'Failure, Out of memory (IPQ_OUTOFMEMORY)',
                       -2: 'Failure, Invalid VAR type (IPQ_BADVARTYPE)',
                       -3: 'Failure, Invalid argument (IPQ_INVALIDARG)',
                       -4: 'Failure, Invalid row (IPQ_INVALIDROW)',
                       -5: 'Failure, Invalid column (IPQ_INVALIDCOL)',
                       -6: 'Failure, Invalid instance id (IPQ_BADINSTANCE)'}

        ipcl = ctypes.cdll.LoadLibrary(self.iPhreeqcLib)

        methods = [('_AccumulateLine', ipcl.AccumulateLine,
                    [ctypes.c_int, ctypes.c_char_p], ctypes.c_int),
                   ('_AddError', ipcl.AddError,
                    [ctypes.c_int, ctypes.c_char_p], ctypes.c_int),
                   ('_AddWarning', ipcl.AddWarning,
                    [ctypes.c_int, ctypes.c_char_p], ctypes.c_int),
                   ('_ClearAccumulatedLines',
                    ipcl.ClearAccumulatedLines, [ctypes.c_int],
                    ctypes.c_int),
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
                   ('_GetDumpFileOn', ipcl.GetDumpFileOn, [ctypes.c_int],
                    ctypes.c_int),
                   ('_GetDumpString', ipcl.GetDumpString, [ctypes.c_int],
                    ctypes.c_char_p),
                   ('_GetDumpStringLine', ipcl.GetDumpStringLine,
                    [ctypes.c_int, ctypes.c_int], ctypes.c_char_p),
                   ('_GetDumpStringLineCount', ipcl.GetDumpStringLineCount,
                    [ctypes.c_int], ctypes.c_int),
                   ('_GetDumpStringOn', ipcl.GetDumpStringOn, [ctypes.c_int],
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
                   ('_GetNthSelectedOutputUserNumber',
                    ipcl.GetNthSelectedOutputUserNumber,
                    [ctypes.c_int, ctypes.c_int], ctypes.c_int),
                   ('_GetOutputString', ipcl.GetOutputString,
                    [ctypes.c_int],  ctypes.c_char_p),
                   ('_GetOutputFileName', ipcl.GetOutputFileName,
                    [ctypes.c_int],  ctypes.c_char_p),
                   ('_GetOutputFileOn', ipcl.GetOutputFileOn,
                    [ctypes.c_int], ctypes.c_int),
                   ('_GetOutputStringLine', ipcl.GetOutputStringLine,
                    [ctypes.c_int, ctypes.c_int], ctypes.c_char_p),
                   ('_GetOutputStringLineCount',
                    ipcl.GetOutputStringLineCount, [ctypes.c_int],
                    ctypes.c_int),
                   ('_GetOutputStringOn', ipcl.GetOutputStringOn,
                    [ctypes.c_int], ctypes.c_int),
                   ('_GetSelectedOutputColumnCount',
                    ipcl.GetSelectedOutputColumnCount, [ctypes.c_int],
                    ctypes.c_int),
                   ('_GetSelectedOutputCount',
                    ipcl.GetSelectedOutputCount, [ctypes.c_int],
                    ctypes.c_int),
                   ('_GetSelectedOutputFileName',
                    ipcl.GetSelectedOutputFileName,
                    [ctypes.c_int],  ctypes.c_char_p),
                   ('_GetSelectedOutputFileOn',
                    ipcl.GetSelectedOutputFileOn, [ctypes.c_int],
                    ctypes.c_int),
                   ('_GetSelectedOutputRowCount',
                    ipcl.GetSelectedOutputRowCount, [ctypes.c_int],
                    ctypes.c_int),
                   ('_GetSelectedOutputString',
                    ipcl.GetSelectedOutputString, [ctypes.c_int],
                    ctypes.c_char_p),
                   ('_GetSelectedOutputStringLine',
                    ipcl.GetSelectedOutputStringLine,
                    [ctypes.c_int, ctypes.c_int], ctypes.c_char_p),
                   ('_GetSelectedOutputStringLineCount',
                    ipcl.GetSelectedOutputStringLineCount, [ctypes.c_int],
                    ctypes.c_int),
                   ('_GetSelectedOutputStringOn',
                    ipcl.GetSelectedOutputStringOn, [ctypes.c_int],
                    ctypes.c_int),
                   ('_GetSelectedOutputValue', ipcl.GetSelectedOutputValue,
                    [ctypes.c_int, ctypes.c_int, ctypes.c_int,
                     ctypes.POINTER(_VAR)], ctypes.c_int),
                   ('_GetVersionString', ipcl.GetVersionString,
                    [ctypes.c_voidp], ctypes.c_char_p),
                   ('_GetWarningString', ipcl.GetWarningString,
                    [ctypes.c_int], ctypes.c_char_p),
                   ('_GetWarningStringLine', ipcl.GetWarningStringLine,
                    [ctypes.c_int, ctypes.c_int], ctypes.c_char_p),
                   ('_GetWarningStringLineCount',
                    ipcl.GetWarningStringLineCount, [ctypes.c_int],
                    ctypes.c_int),
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
                   ('_SetCurrentSelectedOutputUserNumber',
                    ipcl.SetCurrentSelectedOutputUserNumber,
                    [ctypes.c_int, ctypes.c_int], ctypes.c_int),
                   ('_SetDumpFileName', ipcl.SetDumpFileName,
                    [ctypes.c_int, ctypes.c_char_p], ctypes.c_int),
                   ('_SetDumpFileOn', ipcl.SetDumpFileOn,
                    [ctypes.c_int, ctypes.c_int], ctypes.c_int),
                   ('_SetDumpStringOn', ipcl.SetDumpStringOn,
                    [ctypes.c_int, ctypes.c_int], ctypes.c_int),
                   ('_SetErrorFileName', ipcl.SetErrorFileName,
                    [ctypes.c_int, ctypes.c_char_p], ctypes.c_int),
                   ('_SetErrorFileOn', ipcl.SetErrorStringOn,
                    [ctypes.c_int, ctypes.c_int], ctypes.c_int),
                   ('_SetErrorStringOn', ipcl.SetErrorStringOn,
                    [ctypes.c_int, ctypes.c_int], ctypes.c_int),
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
                   ('_SetSelectedOutputFileOn',
                    ipcl.SetSelectedOutputFileOn, [ctypes.c_int,
                                                   ctypes.c_int],
                    ctypes.c_int),
                   ('_SetSelectedOutputStringOn',
                    ipcl.SetSelectedOutputStringOn,
                    [ctypes.c_int, ctypes.c_int], ctypes.c_int)
        ]
        for name, obj, argtypes, restype in methods:
            obj.argtypes = argtypes
            obj.restype = restype
            setattr(self, name, obj)

        self.var = _VAR()
        self.id = ""
        self.CreateIPhreeqc()

        self.database = ""
        self.dumpFileName=self.GetDumpFileName()
        self.errorFileName=self.GetErrorFileName()
        self.iPhreeqcLib_version = self.GetVersionString()
        self.logFileName=self.GetLogFileName()
        self.outputFileName=self.GetOutputFileName()
        self.runFileName=""
        self.selectedOutputFileName=self.GetSelectedOutputFileName()
        self.SetErrorStringOn() # Default to ON for _RaiseException

    def _RaiseIPhreeqcError(self, code, error="unknown error code"):
        """
        Raise an IPhreeqcError exception based on an integer code

        Parameters:
            code, integer error code between -6 to 1; 0 = no error
            error, user defined error message string
        """
        if code in self.errors:
            error = self.errors[code]
            if error == 0:
                return
        else:
            raise IPhreeqcError("%s: %s" % (code, error))
        
        if code < 0:
            raise IPhreeqcError("%s: %s" % (code, error))
        elif code == 1:
            raise IPhreeqcError("%s: %s\n%s" % (code, error,
                                                self.GetErrorString()))
            
    def AccumulateLine(self, line):
        code = self._AccumulateLine(self.id, bytes(line, 'utf-8'))
        if code != 0:
            self._RaiseIPhreeqcError(code)
    
    def AddError(self, error):
        """
        Appends the given error message to the iphreeqc error string  
        buffer
        
        Parameters:
            error, string message to append

        Returns:
            code, the current "error count" if successful
        """
        code = self._AddError(self.id, bytes(error, 'utf-8'))
        if code < 0:
            self._RaiseIPhreeqcError(code)
        else:
            return code

    def AddWarning(self, warning):
        """
        Appends the given warning message to the iphreeqc warning string
        buffer
        
        Parameters:
            warning, string massage to append

        Returns:
            code, the current "warning count" if successful
        """
        code = self._AddWarning(self.id, bytes(warning, 'utf-8'))
        if code < 0:
            self._RaiseIPhreeqcError(code)
        else:
            return code

    def ClearAccumulatedLines(self):
        code = self._ClearAccumulatedLines(self.id)
        if code != 0:
            self._RaiseIPhreeqcError(code)

    def CreateIPhreeqc(self):
        code = self._CreateIPhreeqc(ctypes.c_voidp())
        if code < 0:
            self._RaiseIPhreeqcError(code)
        self.id = code
        
    def DestroyIPhreeqc(self):
        code = self._DestroyIPhreeqc(self.id)
        if code < 0:
            self._RaiseIPhreeqcError(code)

    def GetComponent(self, index):
        """
        Parameters:
            index, zero-based integer index of the component
        
        Returns:
            component, string component name
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
            lidx, integer line index
        
        Returns:
            one line from dump string at line lidx        
        """
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
            lidx, integer line index
        
        Returns:
            one line from error string at line lidx        
        """
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
            lidx, integer line index
        
        Returns:
            one line from log string at line lidx        
        """
        return self._GetLogStringLine(self.id,
                                      lidx).decode('utf-8', errors='ignore')
 
    def GetLogStringLineCount(self):
        return self._GetLogStringLineCount(self.id)
 
    def GetLogStringOn(self):
        return self._GetLogStringOn(self.id)
 
    def GetNthSelectedOutputUserNumber(self, idx):
        """
        Parameters:
            idx, inter index of the iphreeqc internal zero based array 
                 corresponding to the "user number" defined and input by
                 the user.  i.e. if 5 consecutive user numbers from 1 to 
                 5 are input next to the selected_output blocks, then
                 idx 0 = user number 1, idx 1 = user number 2, ..., idx 4
                 = user number 5.

        Returns:
            result, the user number corresponding to idx
        """
        result = self._GetNthSelectedOutputUserNumber(self.id, idx)
        if result < 0:
            self._RaiseIPhreeqcError(result)

        return result
    
    def GetOutputString(self):
        return self._GetOutputString(self.id).decode('utf-8',errors='ignore')
 
    def GetOutputFileName(self):
        return self._GetOutputFileName(self.id).decode('utf-8')
 
    def GetOutputFileOn(self):
        return self._GetOutputFileOn(self.id)
 
    def GetOutputStringLine(self, lidx):
        """
        Parameters:
            lidx, integer line index
        
        Returns:
            one line from output string at line lidx        
        """
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

    def GetSelectedOutputColumn(self, cidx):
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

    def GetSelectedOutputCount(self):
        return self._GetSelectedOutputCount(self.id)

    def GetSelectedOutputFileName(self):
        return self._GetSelectedOutputFileName(self.id).decode('utf-8')
 
    def GetSelectedOutputFileOn(self):
        return self._GetSelectedOutputFileOn(self.id)
 
    def GetSelectedOutputRow(self, ridx):
        """
        Return one row (all columns) from selected output at row index ridx

        Parameters:
            ridx, integer row index (can be negative to index back from the
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

    def GetSelectedOutputString(self):
        return self._GetSelectedOutputString(self.id).decode('utf-8',
                                                             errors='ignore')
 
    def GetSelectedOutputStringLine(self, lidx):
        """
        Parameters:
            lidx, integer line index
        
        Returns:
            one line from output string at line lidx        
        """
        return self._GetSelectedOutputStringLine(self.id,
                                                 lidx).decode('utf-8',
                                                              errors='ignore')
 
    def GetSelectedOutputStringLineCount(self):
        return self._GetSelectedOutputStringLineCount(self.id)
 
    def GetSelectedOutputStringOn(self):
        return self._GetSelectedOutputStringOn(self.id)
 
    def GetSelectedOutputValue(self, ridx, cidx):
        """
        Parameters:
            ridx, integer row index
            cidx, integer column index
        
        Returns:
            val, one selected output value at ridx and cidx
        """
        code = self._GetSelectedOutputValue(self.id, ridx, cidx,
                                            self.var)
        if code != 0:
            self._RaiseIPhreeqcError(code)
            
        if self.var.type == 3:
            val = self.var.value.double_value
        elif self.var.type == 2:
            val = self.var.value.long_value
        elif self.var.type == 4:
            val = self.var.value.string_value.decode('utf-8')
        elif self.var.type == 0:
            val = None

        if self.var.type == 1:
            self._RaiseIPhreeqcError(value.error_code)

        return val

    def GetVersionString(self):
        return self._GetVersionString(self.id).decode('utf-8')

    def GetWarningString(self):
        return self._GetWarningString(self.id).decode('utf-8')

    def GetWarningStringLine(self, lidx):
        """
        Parameters:
            lidx, integer line index
        
        Returns:
            one line from warning string at line lidx        
        """
        return self._GetWarningStringLine(self.id,
                                          lidx).decode('utf-8',
                                                       errors='ignore')
 
    def GetWarningStringLineCount(self):
        return self._GetWarningStringLineCount(self.id)
 
    def LoadDatabase(self, database):
        """
        Parameters:
            database, fully qualified path name string to the iphreeqc
                      database to load.  E.g.,
                      "/<iphreeqc library install PREFIX>
                       /share/doc/iphreeqc/database/phreeqc.dat"
        """
        code = self._LoadDatabase(self.id, bytes(database, 'utf-8'))
        if code == 0:
            self.database=database
        else:
            self._RaiseIPhreeqcError(code)

    def LoadDatabaseString(self, input_string):
        code = self._LoadDatabaseString(self.id,
                                        ctypes.c_char_p(bytes(input_string,
                                                              'utf-8')))
        if code != 0:
            self._RaiseIPhreeqcError(code)

    def OutputAccumulatedLines(self):
        """
        output accumulated lines to stdout (i.e. not inside python)
        """
        self._OutputAccumulatedLines(self.id)
    
    def RunAccumulated(self):
        """
        """
        code = self._RunAccumulated(self.id)
        if code != 0:
            self._RaiseIPhreeqcError(code)
    
    def RunFile(self,runFQPN):
        """
        Parameters:
            runFQPN, fully qualified path name string to a "run" file 
            containing valid phreeqc instructions
        """
        code = self._RunFile(self.id, bytes(runFQPN, 'utf-8'))
        if code == 0:
            self.runFileName=runFQPN
        else:
            self._RaiseIPhreeqcError(code)
            
    def RunString(self, cmd_string):
        """
        Parameters:
            cmd_string, phreeqc command string to be executed
        """
        code = self._RunString(self.id,
                               ctypes.c_char_p(bytes(cmd_string, 'utf-8')))
        if code != 0:
            self._RaiseIPhreeqcError(code)
    
    def SetCurrentSelectedOutputUserNumber(self, unum):
        """
        Parameters:
            unum, integer user number
        """
        code = self._SetCurrentSelectedOutputUserNumber(self.id, unum)
        if code != 0:
            self._RaiseIPhreeqcError(code)
 
    def SetDumpFileName(self,dumpFQPN):
        """
        Parameters:
            dmpFQPN, fully qualified path name string to a dump file
        """
        code = self._SetDumpFileName(self.id,  bytes(dumpFQPN, 'utf-8'))
        if code == 0:
            self.dumpFile = dumpFileFQPN
        else:
            self._RaiseIPhreeqcError(code)
            
    def SetDumpFileOn(self,val=1):
        """
        Parameters:
            val, 0 = OFF; 1 = ON
        """
        code = self._SetDumpFileOn(self.id,val)
        if code != 0:
            self._RaiseIPhreeqcError(code)

    def SetDumpStringOn(self,val=1):
        """
        Parameters:
            val, 0 = OFF; 1 = ON
        """
        code = self._SetDumpStringOn(self.id,val)
        if code != 0:
            self._RaiseIPhreeqcError(code)

    def SetErrorFileName(self,errorFQPN):
        """
        Parameters:
            errFQPN, fully qualified path name string to an error file
        """
        code = self._SetErrorFileName(self.id,  bytes(errorFQPN, 'utf-8'))
        if code == 0:
            self.errorFileName=errorFQPN
        else:
            self._RaiseIPhreeqcError(code)
            
    def SetErrorFileOn(self,val=1):
        """
        Parameters:
            val, 0 = OFF; 1 = ON
        """
        code = self._SetErrorFileOn(self.id,val)
        if code != 0:
            self._RaiseIPhreeqcError(code)

    def SetErrorStringOn(self,val=1):
        """
        Parameters:
            val, 0 = OFF; 1 = ON
        """
        code = self._SetErrorStringOn(self.id,val)
        if code != 0:
            self._RaiseIPhreeqcError(code)

    def SetLogFileName(self,logFQPN):
        """
        Parameters:
            logFQPN, fully qualified path name string to a log file
        """
        code = self._SetLogFileName(self.id,  bytes(logFQPN, 'utf-8'))
        if code == 0:
            self.logFileName=logFQPN
        else:
            self._RaiseIPhreeqcError(code)
            
    def SetLogFileOn(self,val=1):
        """
        Parameters:
            val, 0 = OFF; 1 = ON
        """
        code = self._SetLogFileOn(self.id,val)
        if code != 0:
            self._RaiseIPhreeqcError(code)

    def SetLogStringOn(self,val=1):
        """
        Parameters:
            val, 0 = OFF; 1 = ON
        """
        code = self._SetLogStringOn(self.id,val)
        if code != 0:
            self._RaiseIPhreeqcError(code)

    def SetOutputFileName(self,outputFQPN):
        """
        Parameters:
            outputFQPN, fully qualified path name string to an output file
        """
        code = self._SetOutputFileName(self.id,
                                       bytes(outputFQPN, 'utf-8'))
        if code == 0:
            self.outputFileName = outputFQPN
        else:
            self._RaiseIPhreeqcError(code)
            
    def SetOutputFileOn(self,val=1):
        """
        Parameters:
            val, 0 = OFF; 1 = ON
        """
        code = self._SetOutputFileOn(self.id,val)
        if code != 0:
            self._RaiseIPhreeqcError(code)

    def SetOutputStringOn(self,val=1):
        """
        Parameters:
            val, 0 = OFF, 1 = ON
        """
        code = self._SetOutputStringOn(self.id,val)
        if code != 0:
            self._RaiseIPhreeqcError(code)

    def SetSelectedOutputFileName(self,selectedOutputFQPN):
        """
        Parameters:
            selectedOutFQPN, fully qualified path name string to a selected 
            output file
        """
        code = self._SetSelectedOutputFileName(self.id,
                                               bytes(selectedOutputFQPN,
                                                     'utf-8'))
        if code == 0:
            self.selectedOutputFileName = selectedOutputFQPN
        else:
            self._RaiseIPhreeqcError(code)
            
    def SetSelectedOutputFileOn(self,val=1):
        """
        Parameters:
            val, 0 = OFF; 1 = ON
        """
        code = self._SetSelectedOutputFileOn(self.id, val)
        if code != 0:
            self._RaiseIPhreeqcError(code)
            

    def SetSelectedOutputStringOn(self,val=1):
        """
        Parameters:
            val, 0 = OFF; 1 = ON
        """
        code = self._SetSelectedOutputStringOn(self.id, val)
        if code != 0:
            self._RaiseIPhreeqcError(code)            

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

class IPhreeqcError(Exception):
    """
    User defined python exception

    Example usage external to iphreeqc.py (see
    test_iphreeqc/test_ex4.py):
        import iphreeqc as ipc
        ipcl = ipc.iphreeqc(lib='path/to/lib', 
                            database='path/to/database')
        errorMsg = "iphreeqc-py error code: 2 and message: ALARM!!!"
        code = 2
        try:
            ipcl._RaiseIPhreeqcError(code,error=errorMsg)
        except ipc.IPhreeqcError as ipce:
            print(ipce)
    """
    pass

def ex1_mod(lib="libiphreeqc.so", database="phreeqc.dat"):
    """
    Usage example for iphreeqc.py.  

    Demonstrates:
        * instantiating the iphreeqc class
            - initialize iPhreeqcLib
            - CreateIPhreeqc()
            - GetErrorFileName(), intialize errorFileName
            - GetLogFileName(), initialize logFileName
            - GetDumpFileName(), initialize dumpFileName
            - GetOutputFileName(), initialize outputFileName
            - GetSelectedOutputFileName(), initalize selectedOutputFileName
            - GetVersionString(), initialize iPhreeqcLib_version
        * AccumulateLine(<string>)
        * LoadDatabase(<database_FQPN>) i.e. loading an IPhreeqc database
        * GetDumpString()
        * GetDumpStringOn()
        * GetErrorString()
        * GetErrorStringOn()
        * GetLogString()
        * GetLogStringOn()
        * GetOutputString()
        * GetOutputStringOn()
        * RunAccumulated()
        * SetDumpStringOn([val=0|1])
        * SetErrorStringOn([val=0|1])
        * SetLogStringOn([val=0|1])
        * SetOutputStringOn([val=0|1])
    
    Parameters:
        lib, FQPN to the iphreeqc shared library
        database, FQPN to the iphreeqc database "phreeqc.dat"

    Return:
        ipcl, ex1_mod iphreeqc class instance.  For potential use in an 
              interactive python session

    Notes:
        The input string argument to AccumulateLine is derived from the 
        ex1 file found in the examples directory
    """
    if os.path.isfile(lib):
        ipcl=iphreeqc(lib)
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
    print("iphreeqc-py version: %s" % __version__)
    
    ipcl.AccumulateLine(
    """
    TITLE Example 1.--Add uranium and speciate seawater.
    SOLUTION 1  SEAWATER FROM NORDSTROM AND OTHERS (1979)
        units   ppm
        pH      8.22
        pe      8.451
        density 1.023
        temp    25.0
        redox   O(0)/O(-2)
        Ca              412.3
        Mg              1291.8
        Na              10768.0
        K               399.1
        Fe              0.002
        Mn              0.0002  pe
        Si              4.28
        Cl              19353.0
        Alkalinity      141.682 as HCO3
        S(6)            2712.0
        N(5)            0.29    gfw   62.0
        N(-3)           0.03    as    NH4
        U               3.3     ppb   N(5)/N(-3)
        O(0)            1.0     O2(g) -0.7
    SOLUTION_MASTER_SPECIES
        U       U+4     0.0     238.0290     238.0290
        U(4)    U+4     0.0     238.0290
        U(5)    UO2+    0.0     238.0290
        U(6)    UO2+2   0.0     238.0290
    SOLUTION_SPECIES
        #primary master species for U
        #is also secondary master species for U(4)
        U+4 = U+4
                log_k          0.0
        U+4 + 4 H2O = U(OH)4 + 4 H+
                log_k          -8.538
                delta_h        24.760 kcal
        U+4 + 5 H2O = U(OH)5- + 5 H+
                log_k          -13.147
                delta_h        27.580 kcal
        #secondary master species for U(5)
        U+4 + 2 H2O = UO2+ + 4 H+ + e-
                log_k          -6.432
                delta_h        31.130 kcal
        #secondary master species for U(6)
        U+4 + 2 H2O = UO2+2 + 4 H+ + 2 e-
                log_k          -9.217
                delta_h        34.430 kcal
        UO2+2 + H2O = UO2OH+ + H+
                log_k          -5.782
                delta_h        11.015 kcal
        2UO2+2 + 2H2O = (UO2)2(OH)2+2 + 2H+
                log_k          -5.626
                delta_h        -36.04 kcal
        3UO2+2 + 5H2O = (UO2)3(OH)5+ + 5H+
                log_k          -15.641
                delta_h        -44.27 kcal
        UO2+2 + CO3-2 = UO2CO3
                log_k          10.064
                delta_h        0.84 kcal
        UO2+2 + 2CO3-2 = UO2(CO3)2-2
                log_k          16.977
                delta_h        3.48 kcal
        UO2+2 + 3CO3-2 = UO2(CO3)3-4
                log_k          21.397
                delta_h        -8.78 kcal
    PHASES
        Uraninite
        UO2 + 4 H+ = U+4 + 2 H2O
        log_k          -3.490
        delta_h        -18.630 kcal
    DUMP
      -all
    KNOBS
      -logfile
    END
    """)

    ipcl.SetErrorStringOn()
    print("ErrorStringOn (enabled = 1): %s" % ipcl.GetErrorStringOn())
    ipcl.SetLogStringOn()
    print("LogStringOn (enabled = 1): %s" % ipcl.GetLogStringOn())
    ipcl.SetDumpStringOn()
    print("DumpStringOn (enabled = 1): %s" % ipcl.GetDumpStringOn())
    ipcl.SetOutputStringOn()
    print("OutputStringOn (enabled = 1): %s" % ipcl.GetOutputStringOn())
    
    ipcl.RunAccumulated()
    
    print("\n\n*** Error String ***")
    errStr = ipcl.GetErrorString()
    print(errStr) 

    print("\n\n*** Log String ***\n\n")
    logStr = ipcl.GetLogString()
    print(logStr)

    print("\n\n*** Dump String ***")
    dmpStr = ipcl.GetDumpString()
    print(dmpStr) 

    print("\n\n*** Output String ***")
    outStr = ipcl.GetOutputString()
    print(outStr)

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

    ex1_mod_ = ex1_mod(lib,database)
