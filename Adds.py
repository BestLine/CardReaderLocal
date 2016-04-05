import time
import pyQT5tray

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
        pyQT5tray.show_message()
        error_log = "Ошибка. Ридер не найден"
        log_building = (error_log, time_event)
        error_logging(str(log_building))
    except:
        print("не вывел")
        error_log = "Ошибка вывода системного сообщения"
        log_building = (error_log, time_event)
        error_logging(str(log_building))

"""
script = Card Reader
version = 1.0
autor = Best Line
WithOutHelp = false
"""
