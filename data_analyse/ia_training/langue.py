""" Langue Module for future multilanguage integration
"""

FR = {
    "SCORE_TRAIN":
        lambda score: f"Score d'entrainement = {color_score(score)}",
    "SCORE_TEST":
        lambda score: f"Score de Test = {color_score(score)}",
    "SHAPE_SUMMARY":
        lambda _e_train, _e_test, _classe_train, _classe_test:
            f"""Dimmensions des jeux de données
    - entrée entrainement : \033[1m {str(_e_train)}\033[0m
    - entrée test : \033[1m {str(_e_test)}\033[0m
    - classe entrainement : \033[1m {str(_classe_train)}\033[0m
    - class test : \033[1m {str(_classe_test)}\033[0m
            """,
    "WELCOME_MSG": """
Menu selection fonction:
    - \033[1m\033[96md\033[0m : Sauvegarde des Assets de Test
    - \033[1m\033[96ms\033[0m : Entrainement et récupération du score de l'IA
    - \033[1m\033[96mc\033[0m : Quitter""",
    "MODULE_MSG": "Bienvenu sur le Module IA TRAINING",
    "SAVING_START": "Démarrage de la sauvegarde...",
    "SAVING_COMPLETED": "\033[92m\033[1mSauvegarde complete !\033[0m",
    "SAVING_ASK": "Voulez-vous sauvegarder cette entrainement? (y/n)",
    "RETRY_ASK": "Relancer un entrainement ? (y/n)",
    "SAVENAME_ASK": "Quel nom pour le fichier de sauvegarde :"
}


def color_score(_test_score: float) -> str:
    """Colorisation des valeurs de score dans la console

    Args:
        _test_score (float): score de test

    Returns:
        str: le score avec une couleur selon sa valeur
    """
    if _test_score <= 0.7:
        return f"\033[91m\033[1m{_test_score}\033[0m"
    return f"\033[92m\033[1m{_test_score}\033[0m"


LANG = FR
