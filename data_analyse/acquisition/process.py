""" Process Module : Do multiple acquisition for creating dataset
"""
from os import walk
import time

from .get_data import save_data_csv
from .langue import LANG
from .setup import ACQ_LENGHT, ACQ_PATH


def acquisition(solution_id) -> None:
    """Multiple singla data acquistion for one id situation

    Args:
        solution_id (str): id situation
    """
    last_id = get_last_id(ACQ_PATH, solution_id)
    for i in range(ACQ_LENGHT):
        recalibrate_id = last_id + i + 1
        path = csv_path(ACQ_PATH, solution_id, recalibrate_id)
        step_message(i, ACQ_LENGHT, path)
        time.sleep(0.5)
        save_data_csv(path)
        print("step acquired wait before next")
        # Make multiple data save into csv


def step_message(step, acq_lenght, path) -> None:
    """Print every message before each step

    Args:
        step (str): step number
        acq_lenght (str): number of steps
        path (str): path where data will be saved
    """
    print(
        LANG['DATA_ACQUISITION']['PROCESS']['STEP'](step, acq_lenght, path))


def csv_path(acq_path, solution_id, i) -> str:
    """Create dataset_path

    Args:
        acq_path (str): Acquisition path
        solution_id (str): solution number
        i (i): current step

    Returns:
        str: complete path for csv file
    """
    return acq_path + solution_id + "\\" + str(i) + ".csv"


def get_last_id(acq_path, solution_id) -> int:
    """Getting last csv number

    Args:
        acq_path (str): csv path
        solution_id (str): solution id

    Returns:
        int: last id csv
    """
    fl_id = []

    for (dirpath, dirnames, filenames) in walk(acq_path+solution_id+'\\'):
        dirpath, dirnames  # pylint: disable=pointless-statement  # NOSONAR
        fl_id.extend(filenames)
    if fl_id:
        last_f = fl_id[-1]
        result = last_f.split('.')[0]
        return int(result)
    return 0
