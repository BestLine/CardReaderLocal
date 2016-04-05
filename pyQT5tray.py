from PyQt5 import QtGui, QtWidgets
import Read

def show_message():
    tray.showMessage('Критично', 'Считыватель карт не подключён', 3, 100)

def start_icon():
    global tray
    app = QtWidgets.QApplication([])
    set_icon = QtGui.QIcon('Origin.ico')
    tray = QtWidgets.QSystemTrayIcon(set_icon)
    tray.setToolTip("Reader")
    tray.show()
    Read.init()
    app.exec_()

# Completed

"""
script = Card Reader
version = 1.0
autor = Best Line
WithOutHelp = false
"""