from PyQt5 import QtGui, QtWidgets
import Read_Card_Core

def show_message(): # зарезервировано потому что у меня была идея, но я забыл
    tray.showMessage(' Скрипт работает! ', ' Приложите карту ', 1, 100)

def show_disconnect_reader():
    tray.showMessage('Критично', 'Считыватель карт был отключён', 2, 100)

def start_icon():
    global tray
    app = QtWidgets.QApplication([])
    set_icon = QtGui.QIcon('Origin.ico')
    tray = QtWidgets.QSystemTrayIcon(set_icon)
    tray.setToolTip("Reader")
    tray.show()
    show_message()
    Read_Card_Core.init()
    app.exec_()

# Completed

"""
script = Card Reader
version = 1.0
autor = Best Line
WithOutHelp = false
"""