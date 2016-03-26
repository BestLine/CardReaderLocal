import Read
from smartcard.System import readers

# control code
class ErrorCheck():

    def __init__(self):
        reader = readers()
        if not reader:
            print("Reader NOT CONNECTED")
            print("Connect reader please, and try again")
            exit_app()
        else:
            start_init()

# emergency exit
def exit_app():
    exit()

# launch control
def start_init():
    Read.init()

ErrorCheck()

