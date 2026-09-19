import random
import streamlit as st

from logic_utils import check_guess


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Game Glitch Investigator",
    page_icon="🎮",
    layout="centered"
)


# --------------------------------------------------
# GAME FUNCTIONS
# --------------------------------------------------

def generate_secret_number():
    """Generate a random number between 1 and 100."""
    return random.randint(1, 100)


def reset_game():
    """Reset the game with a new secret number."""
    st.session_state.secret_number = generate_secret_number()
    st.session_state.attempts = 0
    st.session_state.game_won = False


# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------

# Streamlit reruns the entire Python file whenever the user
# interacts with a widget.
#
# Using session_state prevents the secret number from changing
# every time the Submit button is clicked.

if "secret_number" not in st.session_state:
    st.session_state.secret_number = generate_secret_number()

if "attempts" not in st.session_state:
    st.session_state.attempts = 0

if "game_won" not in st.session_state:
    st.session_state.game_won = False


# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title("🎮 Game Glitch Investigator")
st.subheader("The Impossible Guesser")

st.write(
    "I'm thinking of a number between **1 and 100**. "
    "Can you guess what it is?"
)


# --------------------------------------------------
# USER INPUT
# --------------------------------------------------

guess = st.number_input(
    "Enter your guess:",
    min_value=1,
    max_value=100,
    value=50,
    step=1
)


# --------------------------------------------------
# SUBMIT GUESS
# --------------------------------------------------

if st.button("Submit Guess", type="primary"):

    if st.session_state.game_won:
        st.info("You already won! Click **New Game** to play again.")

    else:
        st.session_state.attempts += 1

        result = check_guess(
            guess,
            st.session_state.secret_number
        )

        if result == "correct":
            st.session_state.game_won = True

            st.success(
                f"🎉 Correct! The secret number was "
                f"{st.session_state.secret_number}."
            )

            st.balloons()

        elif result == "higher":
            st.warning("⬆️ Too low! Try a HIGHER number.")

        elif result == "lower":
            st.warning("⬇️ Too high! Try a LOWER number.")


# --------------------------------------------------
# ATTEMPT COUNTER
# --------------------------------------------------

st.write(f"**Attempts:** {st.session_state.attempts}")


# --------------------------------------------------
# NEW GAME BUTTON
# --------------------------------------------------

if st.button("🔄 New Game"):
    reset_game()
    st.rerun()


# --------------------------------------------------
# DEVELOPER DEBUG INFORMATION
# --------------------------------------------------

with st.expander("🛠️ Developer Debug Info"):

    st.write("This information is for testing the game.")

    st.write(
        "**Secret Number:**",
        st.session_state.secret_number
    )

    st.write(
        "**Attempts:**",
        st.session_state.attempts
    )

    st.write(
        "**Game Won:**",
        st.session_state.game_won
    )