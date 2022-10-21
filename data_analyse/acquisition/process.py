""" Process Module : Do multiple acquisition for creating dataset
"""
from .setup import ACQ_LENGHT, ACQ_PATH


def acquisition(solution_id):
    """Multiple singla data acquistion for one id situation

    Args:
        solution_id (int): id situation
    """
    print(solution_id)
    for i in range(ACQ_LENGHT):
        print(i, ACQ_PATH)
        # TODO Make multiple data save into csv

# TODO Make Prompt interface for future dataset
