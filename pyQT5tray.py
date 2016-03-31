from PyQt5 import QtGui, QtWidgets
import Read
# Complete
class Tray_Icon():
    app = QtWidgets.QApplication([])
    set_icon = QtGui.QIcon('Origin.ico')
    tray = QtWidgets.QSystemTrayIcon(set_icon)
    tray.setToolTip("Reader")
    tray.show()
    Read.init()
    tray.showMessage('Критично', 'Считыватель карт не подключён', 3, 100)
    app.exec_()


def out_message(tray):
	tray.showMessage('Критично', 'Считыватель карт не подключён', 3, 100)
