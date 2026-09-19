from logic_utils import check_guess


def test_correct_guess():
    assert check_guess(50, 50) == "correct"


def test_guess_too_low():
    assert check_guess(25, 50) == "higher"


def test_guess_too_high():
    assert check_guess(75, 50) == "lower"


def test_minimum_correct():
    assert check_guess(1, 1) == "correct"


def test_maximum_correct():
    assert check_guess(100, 100) == "correct"