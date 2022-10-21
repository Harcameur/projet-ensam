""" IHM Module: Prompt interface
"""
from .langue import LANG

IDS_SOLUTION = ['0', '1', '2']


def main():
    """Start function IHM for acquisition purpose
    """
    solution = ""
    while solution not in IDS_SOLUTION:
        solution = selecting()
    print(LANG['DATA_ACQUISITION']['IHM']['SELECT_MSG'](solution))
    print(LANG['DATA_ACQUISITION']['IHM']['PREPARING_MSG'])


def selecting():
    """Asking id solution

    Returns:
        str: user input
    """
    print(LANG['DATA_ACQUISITION']['IHM']['WELCOME_MSG'])
    return input()
