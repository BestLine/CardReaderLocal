from smartcard.System import readers
import Tray_Icon
import Error_Logger

def app_init():
    Tray_Icon.start_icon()

reader = readers()
if not list(filter(lambda r: str(r) == 'ACS ACR1281 1S Dual Reader PICC 0', reader)):
    error = "БУМ. Ридер не был найден"
    Error_Logger.critical_message(str(error))
    exit()
else:
    app_init()

# Complete

"""
script = Card Reader
version = 1.0
autor = Best Line
WithOutHelp = false
"""