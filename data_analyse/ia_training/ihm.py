""" IHM Module: Prompt interface for IA_training

.. warning::
    This part is only for development purpose, does NOT use it for production
"""
from .train import train_with_sets
# from .numpyfy_data import convert_panda_to_numpy


CMD_LIST = ["train",  "score"]


def main():
    """Start Ia Prompt interface
    """
    print("ia_training")
    # convert_panda_to_numpy()
    train_with_sets()
