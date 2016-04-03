from smartcard.System import readers
import pyQT5tray

def app_init():
    pyQT5tray.start_icon()

reader = readers()

if not reader:
    print("Считыватель не найден")
    reader_error = "Считыватель не найден"
    exit()
else:
    print("Приложите карту ")
    app_init()

# Complete
