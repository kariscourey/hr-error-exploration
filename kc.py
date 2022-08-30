def raise_an_error(value):

    if value < 0:
        raise ValueError

    return value * 2


def safe_int(value):

    try:
        return int(value)
    except ValueError:
        return None
