def check_guess(guess, secret_number):
    """
    Compare the player's guess with the secret number.

    Parameters:
        guess (int): The number entered by the player.
        secret_number (int): The secret number the player
        is trying to guess.

    Returns:
        str:
            "correct" if the guess equals the secret number.
            "higher" if the player needs to guess higher.
            "lower" if the player needs to guess lower.
    """

    if guess == secret_number:
        return "correct"

    if guess < secret_number:
        return "higher"

    return "lower"