from __future__ import print_function
import time
from smartcard.ReaderMonitoring import ReaderMonitor, ReaderObserver
from smartcard.System import readers
import System_Message

time_event = str(time.ctime(time.time()))

class Reader_Log(ReaderObserver):

    def update(self, observable, actions):
        (addedreaders, removedreaders) = actions

        reader_str = str(addedreaders)
        log_building = "ADDED = " + reader_str, time_event
        System_Message.card_reader_log(str(log_building))

        reader_str = str(removedreaders)
        log_building = "REMOVED = " + reader_str, time_event
        System_Message.card_reader_log(str(log_building))

        while not addedreaders:
            time.sleep(1.5)
            System_Message.show_disconnect()
            reader = readers()
            if list(filter(lambda r: str(r) == 'ACS ACR1281 1S Dual Reader PICC 0', reader)):
                break

def init():
    print("Лог ридеров = ВКЛ")
    readermonitor = ReaderMonitor()
    readerobserver = Reader_Log()
    readermonitor.addObserver(readerobserver)

"""
script = Card Reader
version = 1.1
autor = Best Line
WithOutHelp = false
"""