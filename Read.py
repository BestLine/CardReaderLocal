from smartcard.CardConnectionObserver import ConsoleCardConnectionObserver
from smartcard.CardMonitoring import CardMonitor, CardObserver
from smartcard.util import *
import sys
import input_plug
import time

SELECT = [0xFF, 0xCA, 0x00, 0x00, 0x00]
des = "desfire-"

class selectDFTELECOMObserver(CardObserver):

    def __init__(self):
        self.observer = ConsoleCardConnectionObserver()

    def update(self, observable, actions):
        global read
        (addedcards, removedcards) = actions

        for card in addedcards:
            print("+Inserted: ", toHexString(card.atr, PACK))
            card.connection = card.createConnection()
            card.connection.connect()
            card.connection.addObserver(self.observer)
            apdu = SELECT
            response, sw1, sw2 = card.connection.transmit(apdu)
            print(time.ctime(time.time())) # маркер времени
            formatout = toHexString(response[::-1], PACK)
            readd = des + formatout
            timeevent = time.ctime(time.time())
            readlog = str.lower(readd)
            cardlog = readlog, timeevent
            card_log(str(cardlog)) # вывод лога карт
            input_plug.init(read=str(readd)) # ЗАПУСК ВЫВОДА ИД

        for card in removedcards:
            print("-Removed: ", toHexString(card.atr, PACK))

# complete
def card_log(cardlog): # создание и добавление лога карт
    file = open("Card_log.log", "a")
    file.write(cardlog + '\n')
    file.close()##

# emergency exit
def exit_app():
    exit()

# module init
def init(): # инициализация работы
    cardmonitor = CardMonitor()
    selectobserver = selectDFTELECOMObserver()
    cardmonitor.addObserver(selectobserver)

    if 'win32' == sys.platform: # выход по нажатию
        print('press Enter to exit')
        sys.stdin.read(1)
        cardmonitor.deleteObserver(selectobserver)


