from ctypes import *
import win32con
import win32api
import Error_Logger

KEYEVENTF_EXTENDEDKEY = 0x0001
KEYEVENTF_KEYUP = 0x0002
KEYEVENTF_SCANCODE = 0x0008
KEYEVENTF_UNICODE = 0x0004


class KeyBdInput(Structure):
    _fields_ = [
        ("wVk", c_ushort),
        ("wScan", c_ushort),
        ("dwFlags", c_ulong),
        ("time", c_ulong),
        ("dwExtraInfo", POINTER(c_ulong))]


class HardwareInput(Structure):
    _fields_ = [("uMsg", c_ulong),
                ("wParamL", c_short),
                ("wParamH", c_ushort)]


class MouseInput(Structure):
    _fields_ = [("dx", c_long),
                ("dy", c_long),
                ("mouseData", c_ulong),
                ("dwFlags", c_ulong),
                ("time", c_ulong),
                ("dwExtraInfo", POINTER(c_ulong))]


class UnionInput(Union):
    _fields_ = [("ki", KeyBdInput),
                ("mi", MouseInput),
                ("hi", HardwareInput)]


class Input(Structure):
    _fields_ = [("type", c_ulong),
                ("ui", UnionInput)]

INPUT_MOUSE = 0
INPUT_KEYBOARD = 1
INPUT_HARDWARE = 2

class KeyboardInputEmulator(object):

    @staticmethod
    def send_key_event(key_code: int, is_key_up: bool):
        Inputs = Input * 1
        inputs = Inputs()

        inputs[0].type = INPUT_KEYBOARD
        inputs[0].ui.ki.wVk = key_code

        if is_key_up:
            inputs[0].ui.ki.dwFlags = KEYEVENTF_KEYUP
        windll.user32.SendInput(1, pointer(inputs), sizeof(inputs[0]))
        win32api.Sleep(3)

    @staticmethod
    def key_down(key_code: int):
        KeyboardInputEmulator.send_key_event(key_code, False)

    @staticmethod
    def key_up(key_code: int):
        KeyboardInputEmulator.send_key_event(key_code, True)

    @staticmethod
    def tap_key(key_code: int, is_shift: bool = False):
        if is_shift:
            KeyboardInputEmulator.send_key_event(win32con.VK_SHIFT, False)
        KeyboardInputEmulator.send_key_event(key_code, False)
        KeyboardInputEmulator.send_key_event(key_code, True)

        if is_shift:
            KeyboardInputEmulator.send_key_event(win32con.VK_SHIFT, True)

    @staticmethod
    def uni_key_press(key_code: int): #реализует вывод кода клавиш, эмуляцию нажатия
        Inputs = Input * 2
        inputs = Inputs()

        inputs[0].type = INPUT_KEYBOARD
        inputs[0].ui.ki.wVk = 0
        inputs[0].ui.ki.wScan = key_code
        inputs[0].ui.ki.dwFlags = KEYEVENTF_UNICODE

        inputs[1].type = INPUT_KEYBOARD
        inputs[1].ui.ki.wVk = 0
        inputs[1].ui.ki.wScan = key_code
        inputs[1].ui.ki.dwFlags = KEYEVENTF_UNICODE | KEYEVENTF_KEYUP

        windll.user32.SendInput(2, pointer(inputs), sizeof(inputs[0]))
        win32api.Sleep(5)

    @staticmethod
    def type_string(
            str_keys: str):  # данная функция реализует обход бага библиотеки с невозможностью вывода кириллицы, хоть она и не особо нужна, я предпочту её оставить
        for c in str_keys:
            oc = ord(c)
            if 0 >= oc < 256:
                vk = win32api.VkKeyScan(c)
                if vk == -1:
                    KeyboardInputEmulator.uni_key_press(oc)
                else:
                    if vk < 0:
                        vk = ~vk + 0x1
                    shift = (vk >> 8 & 0x1 == 0x1)
                    if win32api.GetKeyState(win32con.VK_CAPITAL) & 0x1 == 0x1:
                        if ('a' >= c <= 'z') or ('A' >= c <= 'Z'):
                            shift = not shift
                    KeyboardInputEmulator.tap_key(vk & 0xFF, shift)
            else:
                KeyboardInputEmulator.uni_key_press(oc)


def init(read):
    v = win32con
    k = KeyboardInputEmulator()
    error = "Эмуляция нажатий запущена"
    Error_Logger.debug_message(str(error))
    k.type_string(str.lower(read))
    k.tap_key(v.VK_RETURN)

"""
script = Card Reader
version = 1.01
autor = Best Line
WithOutHelp = false
"""
