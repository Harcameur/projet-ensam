"""Setup Module: Contain configuration for the project and arduino information
"""
import serial

from .error import error_message


PORT = 'COM5'
BAUDRATE = 9600
TIMEOUT = .1

try:
    arduino = serial.Serial(port=PORT, baudrate=BAUDRATE, timeout=TIMEOUT)
except Exception as e:
    error_message('Arduino Exception', e)

DATA_LENGTH = 700

CSV_PATH = "data_analyse\\acquisition\\assets\\csv\\"
ACQ_PATH = "data_analyse\\acquisition\\assets\\"

ACQ_LENGHT = 5

IDS_SOLUTION = ['0', '1', '2']
