from cx_Freeze import setup, Executable
import sys




base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="CardReader",
    version="2.0",
    description="Card",

    executables=[Executable("main.pyw", base=base)]
)