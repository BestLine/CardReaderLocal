from smartcard.System import readers
import pyQT5tray

import Read

class ErrorCheck():

    def __init__(self):
        reader = readers()
        if not reader:
            print("Reader NOT CONNECTED")
            print("Connect reader please, and try again")
            Read.exit_app()
        else:
            print("Приложите карту ")
            app_init()


def app_init():
    pyQT5tray.trayIcon()

ErrorCheck()
