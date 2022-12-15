"""Main Module for data_analyse
This is just a starter module for the other, it's the root module.
The information for starting the other module is in the method ``start``.
"""
import argparse


MOD_ERROR = "\033[91m\033[1mErreur module Argument\033[0m :"


def start() -> None:
    """This is the starting function
    it permits to get the starting arguments and to treat it.
    This program is done with multiple module for the data analyse to use it
    type in the terminal in the same folder as ``main.py`` :

    .. parsed-literal::
        python main.py -m <module_name>

    .. tip::
        For example if you want to start acquistion module you have to type
        this instruction in the terminal : ``python main.py -m acquisition``

    .. caution::
        If you want to create a module the start function try to execute the
        ``main`` function from ``ihm.py``

    .. warning::
        Also this type of ihm is used only for development purpose

    Alse there is optional argument like starting function for speeder test.

    .. parsed-literal::
        python main.py -m <module_name> -s <cmd_name>

    .. tip::
        The cmd list is refered in `ihm.py` files on the constant `CMD_LIST`
        for example `main.py -m acquisition -s p` to start directly plotter

    """
    parser = argparse.ArgumentParser(description='Ensam Projet Starter : \
        select a module to start')
    parser.add_argument("-m", "--module", help='\
    module name in data_analyse folder and have ihm.py \
    for example `main.py -m acquisition`')

    parser.add_argument("-s", "--start", help='\
    [Optional] commande name in the module in ihm.py \
    for example `main.py -m acquisition -s a`')

    args = parser.parse_args()

    if not args.module:
        print("This program need execution argument for more information type\
-h or --help")

    if args.module:
        try:
            mod = __import__(args.module + '.ihm', fromlist=[''])
            mod.main(args.start)
        except Exception as exception:  # pylint: disable=W0703
            print(MOD_ERROR + 'mod ask' + args.module, exception)


if __name__ == "__main__":
    start()
