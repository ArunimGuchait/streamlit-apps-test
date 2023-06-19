# Import necessary libraries
import streamlit as st
import random

# Set the title of the app
st.title('Number Guessing Game')

# Generate a random number between 1 and 100
number_to_guess = random.randint(1, 100)

# Create a text input for the user to enter their guess
guess = st.text_input('Enter your guess (between 1 and 100)')

# Check if the user has entered a guess
if guess:
    # Convert the guess to an integer
    guess = int(guess)

    # Check if the guess is correct
    if guess == number_to_guess:
        st.write('Congratulations! You guessed correctly.')
    elif guess < number_to_guess:
        st.write('Too low! Try again.')
    else:
        st.write('Too high! Try again.')
else:
    st.write('Please enter a guess.')
