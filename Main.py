from smartcard.System import readers
import Read
import tray_icon

class ErrorCheck():

    def __init__(self):
        reader = readers()
        if not reader:
            print("Reader NOT CONNECTED")
            print("Connect reader please, and try again")
            exit_app()
        else:
            print("12")
            app_init()

def exit_app():
        exit()

def app_init():
    Read.init()

ErrorCheck()
