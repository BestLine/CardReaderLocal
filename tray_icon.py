from PyQt5 import QtGui, QtWidgets
import reading

def show_message():
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
    reading.init()
    app.exec_()
