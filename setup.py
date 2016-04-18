from cx_Freeze import setup, Executable
import sys

smart = "C:\Python27\Lib\site-packages\smartcard"
build_exe_options = {
    "include_files": ["Origin.ico",
                      "C:\Python34_x32\Lib\site-packages\smartcard",
                      "config.py"]
}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="CardReader",
    version="2.0",
    description="Card",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.pyw", base=base)]
)
