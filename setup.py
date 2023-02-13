import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], "includes": ["tkinter", "PyQt6.QtWidgets", "PyQt6", "pymediainfo, ffmpeg, time, pypresence"]}

build_exe_options  = dict(include_files = ['assets/', 'ffmpeg/', 'main.ui'])

# GUI applications require a different base on Windows (the default is for
# a console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="ToMP4",
    version="1",
    description="mp4 encoder",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base=base, icon="assets/ico2.png")]
)