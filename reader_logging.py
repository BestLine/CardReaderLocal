import time
from smartcard.ReaderMonitoring import ReaderMonitor, ReaderObserver
from smartcard.System import readers
import tray_icon
import logging
import os

homePath = os.getenv('TEMP')
logging.basicConfig(format='%(levelname)-8s [%(asctime)s] %(message)s', level=logging.INFO, filename=homePath + '/card_reader_log.log')
time_event = str(time.ctime(time.time()))

class Reader_Log(ReaderObserver):

    def update(self, observable, actions):
        (addedreaders, removedreaders) = actions

        reader_str = str(addedreaders)
        error = "Ридер подключён - ", reader_str
        logging.info(str(error))

        reader_str = str(removedreaders)
        error = "Ридер отключён - ", reader_str
        logging.info(str(error))

        while not addedreaders:
            time.sleep(1.5)
            tray_icon.show_disconnect_reader()
            reader = readers()
            if list(filter(lambda r: str(r) == 'ACS ACR1281 1S Dual Reader PICC 0', reader)):
                break

def init():
    readermonitor = ReaderMonitor()
    readerobserver = Reader_Log()
    readermonitor.addObserver(readerobserver)
