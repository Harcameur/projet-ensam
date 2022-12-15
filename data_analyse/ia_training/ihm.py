""" IHM Module: Prompt interface for IA_training

.. warning::
    This part is only for development purpose, does NOT use it for production
"""
import sys

from .langue import LANG
from .train import train_with_sets
from .numpyfy_data import save_np_data


CMD_LIST = ["d",  "s", "c"]


def main(args: str = None):
    """main function of the ihm

    Args:
        args (str, optional): Execution argument. Defaults to None.
    """
    print(LANG.get('MODULE_MSG'))

    cmd_selected = ""

    if args:
        cmd_selected = args

    while cmd_selected not in CMD_LIST:
        cmd_selected = selecting_cmd()
    if cmd_selected == 'd':
        data_interface()
    if cmd_selected == 's':
        get_score()
    if cmd_selected == 'c':
        sys.exit()


def selecting_cmd():
    """Asking id solution

    Returns:
        str: user input
    """
    print(LANG.get('WELCOME_MSG'))
    return input()


def data_interface():
    """Saving data interface npfy data
    """
    save_np_data()
    main()


def get_score():
    """Score IA interface to loop main
    """
    train_with_sets()
    main()
