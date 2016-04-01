from smartcard.System import readers
import pyQT5tray

def app_init():
    pyQT5tray.start_icon()

reader = readers()

if not reader:
    print("Reader NOT CONNECTED")
    print("Connect reader please, and try again")
    exit()
else:
    print("Приложите карту ")
    app_init()

# Complete
