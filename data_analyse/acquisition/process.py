""" Process Module : Do multiple acquisition for creating dataset
"""
import time

from .langue import LANG
from .setup import ACQ_LENGHT, ACQ_PATH


def acquisition(solution_id):
    """Multiple singla data acquistion for one id situation

    Args:
        solution_id (str): id situation
    """
    for i in range(ACQ_LENGHT + 1):
        step_message(i, ACQ_LENGHT, ACQ_PATH + solution_id)
        time.sleep(1)
        # Make multiple data save into csv

# Make Prompt interface for future dataset


def step_message(step, acq_lenght, path):
    """Print every message before each step

    Args:
        step (str): step number
        acq_lenght (str): number of steps
        path (str): path where data will be saved
    """
    print(
        LANG['DATA_ACQUISITION']['PROCESS']['STEP'](step, acq_lenght, path),
        end="\r")
