import time
import Tray_Icon
import Error_Logger

time_event = str(time.ctime(time.time()))

def card_reader_log(log_building):
    file = open("reader_log.log", "a")
    file.write(log_building + '\n')
    file.close()

def show_disconnect():
    try:
        error = "Ошибка. Ридер был отключён"
        Error_Logger.critical_message(str(error))
        Tray_Icon.show_disconnect_reader()
    except:
        error = "Ошибка вывода сообщения о не подключённом ридере"
        Error_Logger.error_message(str(error))

"""
script = Card Reader
version = 1.0
autor = Best Line
WithOutHelp = false
"""
