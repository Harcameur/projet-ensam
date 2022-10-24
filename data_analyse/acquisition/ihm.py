""" IHM Module: Prompt interface
"""
from .plotter import plot_data
from .process import acquisition
from .setup import ACQ_PATH, IDS_SOLUTION
from .langue import LANG


CMD_LIST = ["p", "a"]


def main():
    cmd_selected = ""
    while cmd_selected not in CMD_LIST:
        cmd_selected = selecting_cmd()
    if cmd_selected == 'p':
        plotter()
    if cmd_selected == 'a':
        acquisition_start()


def acquisition_start():
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
    print(LANG['DATA_ACQUISITION']['IHM']['WELCOME_ACQ_MSG'])
    return input()


def selecting_cmd():
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


def plotter():
    print(LANG['DATA_ACQUISITION']['IHM']['MENU_PLOTTER'])
    id_solution = ''
    while id_solution not in IDS_SOLUTION:
        id_solution = input("Tapez l'id de solution :")
    file_id = ''
    while file_id != 'c':
        file_id = input(
            "Taper le numéro que vous voulez plotter (c pour quitter) :")
        plot_data(f"{ACQ_PATH}\\{id_solution}\\{file_id}.csv")
