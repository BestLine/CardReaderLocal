import logging
import sys
from smartcard.CardConnectionObserver import ConsoleCardConnectionObserver
from smartcard.CardMonitoring import CardMonitor, CardObserver
from smartcard.Exceptions import ListReadersException
from smartcard.System import readers
from smartcard.scard import SCARD_E_NO_READERS_AVAILABLE, SCARD_E_SERVICE_STOPPED, SCardListReaders
from smartcard.util import *
import smartcard.pcsc.PCSCCardRequest
import config
import input_emulation
import reader_logging

SELECT = [0xFF, 0xCA, 0x00, 0x00, 0x00]
out_prefix = "desfire-"



class Select_Observer(CardObserver):

    def __init__(self):
        super().__init__()
        self.observer = ConsoleCardConnectionObserver()

    def update(self, observable, actions):
        global read
        (addedcards, removedcards) = actions
        reader = readers()
        if not list(filter(lambda r: str(r) in config.IGNORE_READERS, reader)):
            for card in addedcards:
                try:
                    card.connection = card.createConnection()
                    card.connection.connect()
                    card.connection.addObserver(self.observer)
                    response, sw1, sw2 = card.connection.transmit(SELECT)
                    formating_out = toHexString(response[::-1], PACK)
                    create_out = out_prefix + formating_out
                    input_emulation.init(create_out)
                except:

                    def my_handler(type, value, tb):
                        logger.exception("Uncaught exception: {0}".format(str(value)))

                    logger = logging.getLogger('mylogger')
                    sys.excepthook = my_handler

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
    reader_logging.init()
