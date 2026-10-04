# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

The **Impossible Guesser** is a number guessing game built with Python and Streamlit.

The player tries to guess a randomly generated number between **1 and 100**. After each guess, the game tells the player whether they need to guess higher or lower.

The original AI-generated version of the game contained several bugs that made the game difficult or impossible to complete correctly.

The main problems were:

- The secret number could reset when Streamlit reran the application.
- The higher/lower hints could give the player incorrect information.
- Important game logic needed to be separated from the Streamlit user interface so that it could be tested independently.

The goal of this project was to identify these problems, understand why they happened, repair them, and verify the fixes using automated testing.

---

## 🛠️ Setup

### 1. Install the required dependencies

Open a terminal in the project folder and run:

```bash
pip install -r requirements.txt
```

### 2. Start the Streamlit application

Run:

```bash
python -m streamlit run app.py
```

Streamlit will open the game in a web browser.

---

## 🎯 Game Purpose

The purpose of the game is to correctly guess a randomly generated number between **1 and 100**.

The player enters a number and selects **Submit Guess**.

The game responds with one of three results:

- **Too low** — the player needs to guess a higher number.
- **Too high** — the player needs to guess a lower number.
- **Correct** — the player guessed the secret number and wins the game.

The application also keeps track of the number of attempts made during the current game.

---

## 🐛 Bugs I Found

### Bug 1: Secret Number Resetting

Streamlit reruns the entire Python file whenever the user interacts with a widget.

If the secret number is stored in a regular Python variable, a new number can be generated each time the player presses **Submit Guess**.

This means the player could be trying to guess a number that constantly changes.

### Expected Behavior

The secret number should remain the same until the player starts a new game.

### Fix

I stored the secret number inside:

```python
st.session_state.secret_number
```

This allows the secret number to remain unchanged between Streamlit reruns.

---

### Bug 2: Incorrect Higher and Lower Hints

The guessing logic originally had problems determining whether the player needed to guess higher or lower.

For example, if the secret number was `50` and the player guessed `40`, the game should tell the player to guess higher.

### Expected Behavior

```text
Guess: 40
Secret Number: 50
Result: Too low! Try a HIGHER number.
```

If the player guesses `60`:

```text
Guess: 60
Secret Number: 50
Result: Too high! Try a LOWER number.
```

### Fix

I corrected the comparison logic inside `logic_utils.py`.

The final function is:

```python
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
```

---

### Bug 3: Game Logic Mixed With the User Interface

Important guessing logic was originally connected too closely to the Streamlit interface.

This made the program harder to test and maintain.

### Fix

I moved the guess comparison logic into:

```text
logic_utils.py
```

The Streamlit application imports the function using:

```python
from logic_utils import check_guess
```

This separates the game logic from the user interface and makes the function easier to test using `pytest`.

---

## 🔧 Fixes Applied

The final version includes the following improvements:

- [x] Stored the secret number using Streamlit `session_state`
- [x] Prevented the secret number from changing after every guess
- [x] Corrected the higher/lower hint logic
- [x] Moved `check_guess()` into `logic_utils.py`
- [x] Added an attempt counter
- [x] Added a game-won state
- [x] Prevented additional guesses after the player wins
- [x] Added a **New Game** button
- [x] Added developer debug information
- [x] Added automated tests
- [x] Verified the game using `pytest`
- [x] Tested the completed game in Streamlit

---

## 🤖 Working With AI

I used an AI coding assistant as a debugging teammate during this project.

Instead of accepting every suggestion automatically, I reviewed the code and tested the changes before deciding whether they were correct.

One useful suggestion was using Streamlit's `session_state` to store the secret number.

This solved the problem where the application's variables could reset whenever Streamlit reran the Python file.

I also used AI to help analyze the higher/lower logic and organize the `check_guess()` function inside `logic_utils.py`.

After making changes, I verified the behavior myself by running the game and using automated tests.

This project showed me that AI can help identify and explain bugs, but the developer still needs to review, test, and verify the results.

---

## 📸 Demo Walkthrough

The following example demonstrates how the completed game works.

1. The user starts the application with:

```bash
python -m streamlit run app.py
```

2. The game generates a secret number between **1 and 100** and stores it in Streamlit's session state.

3. The user enters a guess of `40`.

```text
Guess: 40
Secret Number: 50
```

The game responds:

```text
⬆️ Too low! Try a HIGHER number.
```

The attempt counter becomes:

```text
Attempts: 1
```

4. The user enters a second guess of `70`.

The game responds:

```text
⬇️ Too high! Try a LOWER number.
```

The attempt counter becomes:

```text
Attempts: 2
```

5. The user enters `50`.

The game responds:

```text
🎉 Correct! The secret number was 50.
```

The attempt counter becomes:

```text
Attempts: 3
```

6. The game records that the player has won and displays the Streamlit celebration balloons.

7. If the player presses **Submit Guess** again, the application displays:

```text
You already won! Click New Game to play again.
```

The attempt counter does not increase.

8. The player can select:

```text
🔄 New Game
```

The program generates a new secret number, resets the attempt counter to `0`, and sets the game-won status back to `False`.

---

## 🧪 Automated Testing

The game logic is tested independently from the Streamlit interface.

Example tests verify all three possible results:

```python
from logic_utils import check_guess


def test_correct_guess():
    assert check_guess(50, 50) == "correct"


def test_guess_too_low():
    assert check_guess(40, 50) == "higher"


def test_guess_too_high():
    assert check_guess(60, 50) == "lower"
```

The tests can be run from the project directory using:

```bash
pytest
```

The tests verify that:

- A correct guess returns `"correct"`.
- A guess below the secret number returns `"higher"`.
- A guess above the secret number returns `"lower"`.

---

## 🧪 Test Results

The automated tests passed successfully.

```text
pytest

============================= test session starts =============================

tests/test_game_logic.py

============================== 5 passed ==============================
```

This confirms that the repaired game logic behaves as expected.

---

## 📁 Project Structure

```text
Game-Glitch-Investigator/
│
├── app.py
├── logic_utils.py
├── requirements.txt
├── README.md
├── reflection.md
│
└── tests/
    └── test_game_logic.py
```

### `app.py`

Contains the Streamlit user interface, session-state management, attempt counter, win state, and New Game functionality.

### `logic_utils.py`

Contains the reusable `check_guess()` game logic.

### `tests/test_game_logic.py`

Contains automated `pytest` tests that verify the guessing logic.

### `reflection.md`

Documents the bugs, debugging process, AI collaboration, testing process, and what I learned from the project.

---

## 🚀 What I Learned

This project helped me understand how debugging requires more than simply finding a line of code that looks wrong.

I learned how to:

- Identify logic bugs.
- Identify problems caused by application state.
- Use `st.session_state` in Streamlit.
- Separate program logic from user-interface code.
- Refactor Python functions into separate files.
- Import functions between Python files.
- Write and run automated tests using `pytest`.
- Verify AI-generated code instead of assuming it is correct.
- Use AI as a coding assistant while still making my own decisions about the code.

The most important lesson was that AI-generated code still needs human review and testing.

---

## ✅ Project Status

- [x] Game runs successfully
- [x] Secret number remains consistent during a game
- [x] Higher/lower hints work correctly
- [x] Attempt counter works
- [x] Winning condition works
- [x] New Game button works
- [x] Logic was moved into `logic_utils.py`
- [x] Automated tests were added
- [x] Tests pass
- [x] README completed
- [x] Reflection completed
- [x] Project ready for final commit and submission

## 🚀 Stretch Features

No additional stretch features were added. The focus of this project was repairing the original bugs, refactoring the game logic, and verifying the final application with automated tests.
