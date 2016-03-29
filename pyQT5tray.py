from PyQt5 import QtGui, QtWidgets
import Read

class trayIcon():
    app = QtWidgets.QApplication([])
    icon = QtGui.QIcon('Origin.ico')
    tray = QtWidgets.QSystemTrayIcon(icon)
    tray.show()
    Read.init()
    app.exec_()

