:: OData Python Client and Server Libraries ver. 1.0.0

:: Copyright (c) Microsoft Corporation
:: All rights reserved. 

## ARE YOU all rights reserved or are you MIT licence -- you can't be both.

:: MIT License

:: Permission is hereby granted, free of charge, to any person obtaining a
:: copy of this software and associated documentation files (the "Software"),
:: to deal in the Software without restriction, including without limitation
:: the rights to use, copy, modify, merge, publish, distribute, sublicense,
:: and/or sell copies of the Software, and to permit persons to whom the
:: Software is furnished to do so, subject to the following conditions:

:: The above copyright notice and this permission notice shall be included
:: in all copies or substantial portions of the Software.

:: THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
:: IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
:: FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
:: AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
:: LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
:: FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
:: DEALINGS IN THE SOFTWARE.

@echo off
if exist "odatacpp\output\Win32\Release\odata_client.vs12.dll" (goto vs12)
if exist "odatacpp\output\Win32\Release\odata_client.vs11.dll" (goto vs11)
goto finish

:vs12
copy odatacpp\msvc\vs12\packages\cpprestsdk.2.1.0\build\native\lib\Win32\v120\Release\Desktop\cpprest120_2_1.lib cpprest_2_1.lib
copy odatacpp\output\Win32\Release\odata_client.vs12.lib odata_client.lib
CL.exe /c /I%PYTHON_INCLUDE% /Iodatacpp\include /Iodatacpp\msvc\vs11\packages\cpprestsdk.2.1.0\build\native\include /Iodatacpp\msvc\vs12\packages\cpprestsdk.2.1.0\build\native\include /nologo /O2 /Oi /Oy- /GL /D HAS_CPPRESTSDK /D SWIG_PYTHON_INTERPRETER_NO_DEBUG /D WIN32 /D _USRDLL /D COMMONTESTS_EXPORTS /D _WINDLL /D _UNICODE /D UNICODE /Gm- /EHsc /MD /GS /Gy /fp:precise /Zc:wchar_t /Zc:forScope /Gd /TP /Zm200 odata_client_python_wrap.cxx
link.exe /OUT:"_odata_client_python.pyd" /INCREMENTAL:NO /NOLOGO cpprest_2_1.lib %PYTHON_LIB% kernel32.lib user32.lib gdi32.lib winspool.lib comdlg32.lib advapi32.lib shell32.lib ole32.lib oleaut32.lib uuid.lib odbc32.lib odbccp32.lib odata_client.lib /MANIFEST /MANIFESTUAC:"level='asInvoker' uiAccess='false'" /manifest:embed /DEBUG /PDB:"_odata_client_python.pdb" /OPT:REF /OPT:ICF /LTCG /TLBID:1 /DYNAMICBASE /NXCOMPAT /IMPLIB:"_odata_client_python.lib" /MACHINE:X86 /SAFESEH /DLL odata_client_python_wrap.obj
copy odatacpp\output\Win32\Release\cpprest120_2_1.dll .
copy odatacpp\output\Win32\Release\odata_client.vs12.dll .
goto clean

:vs11
copy odatacpp\msvc\vs11\packages\cpprestsdk.2.1.0\build\native\lib\Win32\v110\Release\Desktop\cpprest110_2_1.lib cpprest_2_1.lib
copy odatacpp\output\Win32\Release\odata_client.vs11.lib odata_client.lib
CL.exe /c /I%PYTHON_INCLUDE% /Iodatacpp\include /Iodatacpp\msvc\vs11\packages\cpprestsdk.2.1.0\build\native\include /Iodatacpp\msvc\vs12\packages\cpprestsdk.2.1.0\build\native\include /nologo /O2 /Oi /Oy- /GL /D HAS_CPPRESTSDK /D SWIG_PYTHON_INTERPRETER_NO_DEBUG /D WIN32 /D _USRDLL /D COMMONTESTS_EXPORTS /D _WINDLL /D _UNICODE /D UNICODE /Gm- /EHsc /MD /GS /Gy /fp:precise /Zc:wchar_t /Zc:forScope /Gd /TP /Zm200 odata_client_python_wrap.cxx
link.exe /OUT:"_odata_client_python.pyd" /INCREMENTAL:NO /NOLOGO cpprest_2_1.lib %PYTHON_LIB% kernel32.lib user32.lib gdi32.lib winspool.lib comdlg32.lib advapi32.lib shell32.lib ole32.lib oleaut32.lib uuid.lib odbc32.lib odbccp32.lib odata_client.lib /MANIFEST /MANIFESTUAC:"level='asInvoker' uiAccess='false'" /manifest:embed /DEBUG /PDB:"_odata_client_python.pdb" /OPT:REF /OPT:ICF /LTCG /TLBID:1 /DYNAMICBASE /NXCOMPAT /IMPLIB:"_odata_client_python.lib" /MACHINE:X86 /SAFESEH /DLL odata_client_python_wrap.obj
copy odatacpp\output\Win32\Release\cpprest110_2_1.dll .
copy odatacpp\output\Win32\Release\odata_client.vs11.dll .
goto clean

:clean
if exist "cpprest_2_1.lib" (del cpprest_2_1.lib)
if exist "odata_client.lib" (del odata_client.lib)
if exist "_odata_client_python.exp" (del _odata_client_python.exp)
if exist "_odata_client_python.lib" (del _odata_client_python.lib)
if exist "_odata_client_python.pdb" (del _odata_client_python.pdb)
if exist "odata_client_python_wrap.obj" (del odata_client_python_wrap.obj)
goto finish

:finish
