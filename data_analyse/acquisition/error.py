"""Error Module: Manage issue
"""


def error_message(tag, exception):
    """Send custom error message tag + detail

    Args:
        tag (str): exception tag custom by situration
        exception (str): exception detail
    """
    print(f"\033[91m\033[1m{tag}\033[0m :", exception)
