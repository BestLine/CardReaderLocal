from PyQt5 import QtGui, QtWidgets
import Read_Card_Core

def show_message():
    tray.showMessage('Критично', 'Считыватель карт не подключён', 3, 100)

def show_disconnect_reader():
    tray.showMessage('Критично', 'Считыватель карт был отключён', 2, 100)

def start_icon():
    global tray
    app = QtWidgets.QApplication([])
    set_icon = QtGui.QIcon('Origin.ico')
    tray = QtWidgets.QSystemTrayIcon(set_icon)
    tray.setToolTip("Reader")
    tray.show()
    Read_Card_Core.init()
    app.exec_()

# Completed

"""
script = Card Reader
version = 1.0
autor = Best Line
WithOutHelp = false
"""