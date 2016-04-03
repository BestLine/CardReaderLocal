from smartcard.CardConnectionObserver import ConsoleCardConnectionObserver
from smartcard.CardMonitoring import CardMonitor, CardObserver
from smartcard.util import *
import input_plug
import time
import Adds
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
    Adds.show()

def init():

    card_monitor = CardMonitor()
    select_observer = Select_Observer()
    card_monitor.addObserver(select_observer)

# Complete
