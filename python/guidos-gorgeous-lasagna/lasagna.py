EXPECTED_BAKE_TIME = 40

def bake_time_remaining(elapsed_time):
    """Return remaining bake time.

    :param elapsed_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) based on EXPECTED_BAKE_TIME.
    """
    return EXPECTED_BAKE_TIME - elapsed_time

def preparation_time_in_minutes(number_of_layers):
    """Return preparation time based on number of layers.

    :param number_of_layers: int - the number of lasagna layers.
    :return: int - total preparation time (in minutes).
    """
    return number_of_layers * 2

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed cooking time.

    :param number_of_layers: int - the number of layers in the lasagna.
    :param elapsed_bake_time: int - elapsed cooking time.
    :return: int - total time elapsed (in minutes) preparing and cooking.

    This function takes two integers representing the number of lasagna layers and the
    time already spent baking and calculates the total elapsed minutes spent cooking the
    lasagna.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time