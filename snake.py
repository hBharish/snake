import streamlit as st
import time
import random

# Set up the game board
WIDTH, HEIGHT = 20, 20

# Initialize the snake
snake = [(0, 0)]
snake_direction = (0, 1)
snake_growth = 0

# Initialize the food
food = (random.randint(0, WIDTH - 1), random.randint(0, HEIGHT - 1))

# Initialize game over flag
game_over = False

# Function to update the game state
def update_game():
    global snake, snake_direction, snake_growth, food, game_over

    if game_over:
        st.write("Game Over! Press Restart to play again.")
        return

    # Move the snake
    new_head = (snake[0][0] + snake_direction[0], snake[0][1] + snake_direction[1])

    # Check for collisions
    if (
        new_head in snake[1:]
        or new_head[0] < 0
        or new_head[0] >= WIDTH
        or new_head[1] < 0
        or new_head[1] >= HEIGHT
    ):
        game_over = True
        return

    snake = [new_head] + snake[:]

    # Check for food
    if new_head == food:
        snake_growth += 1
        food = (random.randint(0, WIDTH - 1), random.randint(0, HEIGHT - 1))

    # Keep the snake length
    if snake_growth == 0:
        snake.pop()

# Streamlit UI
st.title("Snake Game")

if st.button("Restart"):
    snake = [(0, 0)]
    snake_direction = (0, 1)
    snake_growth = 0
    food = (random.randint(0, WIDTH - 1), random.randint(0, HEIGHT - 1))
    game_over = False

st.write("Use the arrow keys to control the snake.")
st.write("Eat the food to grow and score points.")
st.write("Avoid running into the walls or yourself.")

# Main game loop
while not game_over:
    update_game()

    # Display the game board
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if (x, y) in snake:
                st.write("🟩", end="")
            elif (x, y) == food:
                st.write("🍎", end="")
            else:
                st.write("⬜️", end="")
        st.write("")

    time.sleep(0.1)
