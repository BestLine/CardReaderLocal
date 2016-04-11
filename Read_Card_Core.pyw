"""
script      = Card Reader
version     = 1.2
autor       = Best Line
WithOutHelp = false
"""

from smartcard.CardConnectionObserver import ConsoleCardConnectionObserver
from smartcard.CardMonitoring import CardMonitor, CardObserver
from smartcard.Exceptions import ListReadersException
from smartcard.scard import SCARD_E_NO_READERS_AVAILABLE, SCARD_E_SERVICE_STOPPED, SCardListReaders
from smartcard.util import *
import smartcard.pcsc.PCSCCardRequest
import Reader_Log
from ctypes import *
import win32con
import win32api
import logging

logging.basicConfig(format='%(levelname)-8s [%(asctime)s] %(message)s', level=logging.INFO, filename='error_log.log')
SELECT = [0xFF, 0xCA, 0x00, 0x00, 0x00]
out_prefix = "desfire-"

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

class Select_Observer(CardObserver):

    def __init__(self):
        super().__init__()
        self.observer = ConsoleCardConnectionObserver()

    def update(self, observable, actions):
        global read
        (addedcards, removedcards) = actions

        for card in addedcards:
            card.connection = card.createConnection()
            card.connection.connect()
            card.connection.addObserver(self.observer)
            response, sw1, sw2 = card.connection.transmit(SELECT)
            formating_out = toHexString(response[::-1], PACK)
            create_out = out_prefix + formating_out
            v = win32con
            k = KeyboardInputEmulator()
            error = "Эмуляция нажатий запущена"
            logging.debug(str(error))
            k.type_string(str.lower(create_out))
            k.tap_key(v.VK_RETURN)

def init():

    def getReaderNames(self): # Здесь мы переопределяем библиотечную функцию для защиты от падений. Было добавлено новое условие по сравнению со стандартной

        hresult, pcscreaders = SCardListReaders(self.hcontext, [])
        if 0 != hresult and SCARD_E_NO_READERS_AVAILABLE and SCARD_E_SERVICE_STOPPED != hresult:
            raise ListReadersException(hresult)

        readers = []

        if None == self.readersAsked:
            readers = pcscreaders
        else:
            for reader in self.readersAsked:
                if not isinstance(reader, type("")):
                    reader = str(reader)
                if reader in pcscreaders:
                    readers = readers + [reader]
        return readers

    smartcard.pcsc.PCSCCardRequest.PCSCCardRequest.getReaderNames = getReaderNames
    card_monitor = CardMonitor()
    select_observer = Select_Observer()
    card_monitor.addObserver(select_observer)
    error = "Считывание запущено"
    logging.debug(str(error))
    Reader_Log.init()

