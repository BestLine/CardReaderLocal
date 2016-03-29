import win32api
import win32con
import win32gui
import Read

class Taskbar:

    def __init__(self): # создание класса windows
        self.visible = 0
        message_map = {
            win32con.WM_DESTROY: self.onDestroy,
            win32con.WM_USER + 20: self.onTaskbarNotify,
        }
        wc = win32gui.WNDCLASS()
        hinst = wc.hInstance = win32api.GetModuleHandle(None)
        wc.lpszClassName = "NewTaskbar"
        wc.style = win32con.CS_VREDRAW | win32con.CS_HREDRAW;
        wc.hCursor = win32gui.LoadCursor(0, win32con.IDC_ARROW)
        wc.hbrBackground = win32con.COLOR_WINDOW
        wc.lpfnWndProc = message_map
        classAtom = win32gui.RegisterClass(wc)
        # создание окна
        style = win32con.WS_OVERLAPPED | win32con.WS_SYSMENU
        self.hwnd = win32gui.CreateWindow(classAtom, "Taskbar", style, \
                    0, 0, win32con.CW_USEDEFAULT, win32con.CW_USEDEFAULT, \
                    0, 0, hinst, None)
        win32gui.UpdateWindow(self.hwnd)

    def setIcon(self, hicon, tooltip=None): # переопределение параметров иконки
        self.hicon = hicon
        self.tooltip = tooltip

    def show(self): # вывод иконки в трей
        flags = win32gui.NIF_ICON | win32gui.NIF_MESSAGE

        if self.tooltip is not None:
            flags |= win32gui.NIF_TIP
            nid = (self.hwnd, 0, flags, win32con.WM_USE + 20, self.hicon, self.tooltip)
        else:
            nid = (self.hwnd, 0, flags, win32con.WM_USER + 20, self.hicon)
        if self.visible:
            self.hide()
        win32gui.Shell_NotifyIcon(win32gui.NIM_ADD, nid)
        self.visible = 1

    def hide(self): # скрытие иконки по дефолту

        if self.visible:
            nid = (self.hwnd, 0)
            win32gui.Shell_NotifyIcon(win32gui.NIM_DELETE, nid)
        self.visible = 0

    def onDestroy(self, hwnd, msg, wparam, lparam):
        self.hide()
        win32gui.PostQuitMessage(0) # закрытие приложения

    def onTaskbarNotify(self, hwnd, msg, wparam, lparam): # выход на двойной клик, действие на одиночный клик пока не задано
        if lparam == win32con.WM_LBUTTONUP:
            self.onClick()

        elif lparam == win32con.WM_LBUTTONDBLCLK:
            self.onDoubleClick()
            win32gui.PostQuitMessage(0)
        return 1


class InitTaskbar(Taskbar):

    def __init__(self): # основной запуск иконки
        Taskbar.__init__(self)
        icon = win32gui.LoadIcon(0, win32con.IDI_APPLICATION)
        self.setIcon(icon)
        self.show()
        Read.init()
        win32gui.PumpMessages()

    def onClick(self): # оповещение о событии
        print("клик")

    def onDoubleClick(self): # оповещение о событии
        print("закрытие при двойном клике!")
