import pyQT5tray

def show():
    print("пробую..")
    try:
        pyQT5tray.show_message()
    except Exception:
        print("не вывел")
