from smartcard.System import readers
import Tray_Icon

reader = readers()

def app_init():
    Tray_Icon.start_icon()

if not reader:
    print("Считыватель не найден")
    reader_error = "Считыватель не найден"
    exit()
else:
    print("Приложите карту ")
    app_init()

# Complete

"""
script = Card Reader
version = 1.0
autor = Best Line
WithOutHelp = false
"""