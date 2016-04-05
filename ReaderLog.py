from __future__ import print_function
import time
from smartcard.ReaderMonitoring import ReaderMonitor, ReaderObserver
import Adds

time_event = str(time.ctime(time.time()))

class Reader_Log(ReaderObserver):

    def update(self, observable, actions):
        (addedreaders, removedreaders) = actions

        reader_str = str(addedreaders)
        log_building = "ADDED = " + reader_str, time_event
        Adds.card_reader_log(str(log_building))

        reader_str = str(removedreaders)
        log_building = "REMOVED = " + reader_str, time_event
        Adds.card_reader_log(str(log_building))

        if not addedreaders:
            Adds.show_disconnect()

def init():
    print("Лог ридеров = ВКЛ")
    readermonitor = ReaderMonitor()
    readerobserver = Reader_Log()
    readermonitor.addObserver(readerobserver)

"""
script = Card Reader
version = 1.0
autor = Best Line
WithOutHelp = false
"""