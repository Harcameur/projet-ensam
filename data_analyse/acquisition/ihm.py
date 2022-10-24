""" IHM Module: Prompt interface
"""
from .process import acquisition
from .setup import IDS_SOLUTION
from .langue import LANG


def main():
    """Start function IHM for acquisition purpose
    """
    solution = ""
    while solution not in IDS_SOLUTION:
        solution = selecting()
    print(LANG['DATA_ACQUISITION']['IHM']['SELECT_MSG'](solution))
    start_acquisition(solution)


def selecting():
    """Asking id solution

    Returns:
        str: user input
    """
    print(LANG['DATA_ACQUISITION']['IHM']['WELCOME_MSG'])
    return input()


def start_acquisition(solution):
    """Start Acquisition process, control and give protocol

    Args:
        solution (str): id_solution numero
    """
    confirm("")
    acquisition(solution)


def confirm(msg):
    """Confirmation message with keypressing wait for next step

    Args:
        msg (str): message printed before keypress
    """
    print(msg)
    input(LANG['NOTIFICATION_MESSAGE']['CONFIRM_MESSAGE'])
