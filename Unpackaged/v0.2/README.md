# Version 0.2 Pyinstaller Files

All files associated with Pyinstaller will be located in the folders seen here. As of version 0.1 the Scipy Module will fail to import the "x.gfortran-win32" modules required to compile the code. The missing DLLs are found in the Scipy folder under the python insall directory.  I am hoping to modify the SPEC files to eventually fix this problem naturally without having to move the DLLs around manually.  

##### To fix this error do the following:
- Find the python install directory (or locate the folder named "gfortran DLLs" one level up)
- Copy the DLLs with the name x.gfortran-win32.dll to the folders which Pyinstaller is trying to find the DLLs in.
- After moving the DLLs, use the SPEC file for the version which corrsponds to the one you are compiling and run pyinstaller.  

