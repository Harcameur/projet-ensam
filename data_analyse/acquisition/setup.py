"""Setup Module: Contain configuration for the project and arduino information
"""
import serial

from .error import error_message


PORT = 'COM5'
BAUDRATE = 9600
TIMEOUT = .1

DATA_LENGTH = 2000

CSV_PATH = "data_analyse\\acquisition\\assets\\csv\\"
ACQ_PATH = "data_analyse\\acquisition\\assets\\data\\"

ACQ_LENGHT = 5

IDS_SOLUTION = ['0', '1', '2']


def arduino_setup():
    """Connecting to the arduino COM port

    Returns:
        serial.Serial: serial object to interact with the arduino
    """
    try:
        return serial.Serial(port=PORT, baudrate=BAUDRATE, timeout=TIMEOUT)
    except Exception as exception:  # pylint: disable=W0703
        error_message('Arduino Exception', exception)
        return None


arduino = arduino_setup()
