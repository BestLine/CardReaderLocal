from smartcard.System import readers
import pyQT5tray
import Read

class Error_Check():

        reader = readers()
        if not reader:
            print("Reader NOT CONNECTED")
            print("Connect reader please, and try again")
            Read.exit_app()
        else:
            print("Приложите карту ")
            app_init()


def app_init():
    pyQT5tray.Tray_Icon()

Error_Check()
# Complete
