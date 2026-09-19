def check_guess(guess, secret_number):
    """
    Compare the player's guess with the secret number.

    Returns:
        "correct" if the guess is correct
        "higher" if the player needs to guess higher
        "lower" if the player needs to guess lower
    """

    if guess == secret_number:
        return "correct"

    elif guess < secret_number:
        return "higher"

    else:
        return "lower"