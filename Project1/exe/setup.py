import os
import sys
from cx_Freeze import setup, Executable

# build_exe_options = {"packages": ["os"], "excludes": ["tkinter"]}
os.environ['TCL_LIBRARY'] = r'c:\Anaconda3\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'c:\Anaconda3\tcl\tk8.6'

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(
    packages = [],
    excludes = [],
    include_files=[r'c:\Anaconda3\DLLs\tcl86t.dll', r'c:\Anaconda3\DLLs\tk86t.dll']
)

base = 'Win32GUI' if sys.platform=='win32' else None

# setup(  name = "tkinter",
#         version = "0.1",
#         description = "My GUI application!",
#         options = {"build_exe": build_exe_options},
#         executables = [Executable("tk_gui.py", base=base)])


executables = [
    Executable('tk_gui.py', base=base)
]

setup(name='tkinter',
      version = '1.0',
      description = 'gui app',
      options = dict(build_exe = buildOptions),
      executables = executables)
