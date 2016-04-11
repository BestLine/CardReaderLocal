"""
script = Card Reader
version = 1.1
autor = Best Line
WithOutHelp = false
"""
from PyQt5 import QtGui, QtWidgets
import Read_Card_Core
import logging

logging.basicConfig(format='%(levelname)-8s [%(asctime)s] %(message)s', level=logging.INFO, filename='error_log.log')

def show_message(): # зарезервировано потому что у меня была идея, но я забыл
    tray.showMessage(' Скрипт работает! ', ' Приложите карту ', 1, 100)

def show_disconnect():
    logging.warning(str("Ошибка. Ридер был отключён"))
    tray.showMessage('Критично', 'Считыватель карт был отключён', 2, 100)

def start_icon():
    global tray
    app = QtWidgets.QApplication([])
    set_icon = QtGui.QIcon('Origin.ico')
    tray = QtWidgets.QSystemTrayIcon(set_icon)
    tray.setToolTip("Reader")
    tray.show()
    logging.debug(str("Иконка трея успешно выведена"))
    show_message()
    Read_Card_Core.init()
    app.exec_()
