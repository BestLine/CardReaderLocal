import time
import Tray_Icon

time_event = str(time.ctime(time.time()))

def card_reader_log(log_building):
    file = open("reader_log.log", "a")
    file.write(log_building + '\n')
    file.close()

def error_logging(log_building):
    file = open("error_log.log", "a")
    file.write(log_building + '\n')
    file.close()

def show():
    print("пробую..")
    try:
        Tray_Icon.show_message()
        error_log = "Ошибка. Ридер не найден"
        log_building = (error_log, time_event)
        error_logging(str(log_building))
    except:
        print("не вывел")
        error_log = "Ошибка вывода системного сообщения"
        log_building = (error_log, time_event)
        error_logging(str(log_building))

def show_disconnect():
    print("Ридер был отключён")
    try:
        Tray_Icon.show_disconnect_reader()
    except:
        print("ошибка вывода сообщения")
        error_log = "Ошибка вывода сообщения о не подключённом ридере"
        log_building = (error_log, time_event)
        error_logging(str(log_building))


"""
script = Card Reader
version = 1.0
autor = Best Line
WithOutHelp = false
"""
