from smartcard.System import readers
import tray_icon
import Read

class ErrorCheck():

    def __init__(self):
        reader = readers()
        if not reader:
            print("Reader NOT CONNECTED")
            print("Connect reader please, and try again")
            Read.exit_app()
        else:
            print("12")
            app_init()


def app_init():
    tray_icon.InitTaskbar()

ErrorCheck()
