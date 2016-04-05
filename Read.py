from smartcard.CardConnectionObserver import ConsoleCardConnectionObserver
from smartcard.CardMonitoring import CardMonitor, CardObserver
from smartcard.Exceptions import ListReadersException
from smartcard.scard import SCARD_E_NO_READERS_AVAILABLE, SCARD_E_SERVICE_STOPPED, SCardListReaders
from smartcard.util import *
import smartcard.pcsc.PCSCCardRequest
import input_plug
import time
import ReaderLog

SELECT = [0xFF, 0xCA, 0x00, 0x00, 0x00]
out_prefix = "desfire-"

class Select_Observer(CardObserver):

    def __init__(self):
        super().__init__()
        self.observer = ConsoleCardConnectionObserver()


    def update(self, observable, actions):
        global read
        (addedcards, removedcards) = actions

        for card in addedcards:
            print("+Inserted: ", toHexString(card.atr, PACK))
            card.connection = card.createConnection()
            card.connection.connect()
            card.connection.addObserver(self.observer)
            response, sw1, sw2 = card.connection.transmit(SELECT)
            print(time.ctime(time.time()))
            formating_out = toHexString(response[::-1], PACK)
            create_out = out_prefix + formating_out
            time_event = time.ctime(time.time())
            read_log = str.lower(create_out)
            create_log = read_log, time_event
            input_plug.init(read=str(create_out))
            card_logging(str(create_log))

        for card in removedcards:
            print("-Removed: ", toHexString(card.atr, PACK))


def card_logging(create_log):
    file = open("card_log.log", "a")
    file.write(create_log + '\n')
    file.close()

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
    print("Лог карт = ВКЛ")
    card_monitor = CardMonitor()
    select_observer = Select_Observer()
    card_monitor.addObserver(select_observer)
    ReaderLog.init()
# Complete

"""
script = Card Reader
version = 1.0
autor = Best Line
WithOutHelp = false
"""