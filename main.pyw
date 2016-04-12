"""
script      = Card Reader
version     = 2.0
autor       = Best Line
WithOutHelp = false
"""
import logging
from smartcard.System import readers
from tendo.singleton import SingleInstance
import tray_icon

logging.basicConfig(format='%(levelname)-8s [%(asctime)s] %(message)s', level=logging.INFO, filename='error_log.log')
me = SingleInstance() # защита от повторного запуска
reader = readers()
logging.debug(str("Скрипт запущен"))
tray_icon.start_icon()


