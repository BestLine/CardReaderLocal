from smartcard.System import readers
from tendo.singleton import SingleInstance
import Tray_Icon
import Error_Logger

def app_init():
    Tray_Icon.start_icon()

me = SingleInstance() # защита от повторного запуска
reader = readers()
if not list(filter(lambda r: str(r) == 'ACS ACR1281 1S Dual Reader PICC 0', reader)):
    error = "БУМ. Ридер не был найден"
    Error_Logger.critical_message(str(error))
    exit()
else:
    error = "Скрипт запущен"
    Error_Logger.debug_message(str(error))
    app_init()

# Complete

"""
script = Card Reader
version = 1.2
autor = Best Line
WithOutHelp = false
"""
