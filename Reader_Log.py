from __future__ import print_function
import time
from smartcard.ReaderMonitoring import ReaderMonitor, ReaderObserver
from smartcard.System import readers
import Error_Logger
import System_Message

time_event = str(time.ctime(time.time()))

class Reader_Log(ReaderObserver):

    def update(self, observable, actions):
        (addedreaders, removedreaders) = actions

        reader_str = str(addedreaders)
        error = "Ридер подключён - ", reader_str
        Error_Logger.info_message(str(error))

        reader_str = str(removedreaders)
        error = "Ридер отключён - ", reader_str
        Error_Logger.info_message(str(error))

        while not addedreaders:
            time.sleep(1.5)
            System_Message.show_disconnect()
            reader = readers()
            if list(filter(lambda r: str(r) == 'ACS ACR1281 1S Dual Reader PICC 0', reader)):
                break

def init():
    readermonitor = ReaderMonitor()
    readerobserver = Reader_Log()
    readermonitor.addObserver(readerobserver)
    error = "Мониторинг ридеров запущен"
    Error_Logger.debug_message(str(error))

"""
script = Card Reader
version = 1.1
autor = Best Line
WithOutHelp = false
"""