""" Langue Module for future multilanguage integration
"""


FR = {
    "DATA_ACQUISITION": {
        "STARTING_MSG": "Démarrage de l'acquisition",
        "FINISH_MSG": "Acquisition fini !",
        "IHM": {
            "WELCOME_ACQ_MSG": """
Menu Acquisition choisissez un identifiant:
    - \033[1m\033[96m0\033[0m : aucune action
    - \033[1m\033[96m1\033[0m : action serrer
    - \033[1m\033[96m2\033[0m : action écarter""",
            "WELCOME_MSG": """
Menu selection fonction:
    - \033[1m\033[96mp\033[0m : Le plotter
    - \033[1m\033[96ma\033[0m : Acquisition de données
    - \033[1m\033[96mc\033[0m : Quitter""",
            "ACQUISITION_MSG": lambda id, current, acq_lenght:
                f"Acquisition de la solution {id} : ({current}/{acq_lenght}):",
            "SELECT_MSG": lambda id:
                f"Id de solution choisi: \033[1m\033[96m{id}\033[0m",
            "PREPARING_MSG": "Preparez vous au début de l'acquistion ...",
            "MENU_PLOTTER": """Menu plotter :
    - \033[1m\033[96m0\033[0m : aucune action
    - \033[1m\033[96m1\033[0m : action serrer
    - \033[1m\033[96m2\033[0m : action écarter""",
        },
        "PROCESS": {
            "STEP": lambda step, acq_lenght, path:
                f"({step}/{acq_lenght}) - {path}",
            "1": """
Pour l'acquisition suivante """,
        }
    },
    "NOTIFICATION_MESSAGE": {
        "CONFIRM_MESSAGE": "Appuyer sur entrer pour continuer ..."
    }
}

LANG = FR
