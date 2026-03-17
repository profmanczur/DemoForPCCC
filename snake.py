import tkinter as tk
import random
import dis
# Constants for the game
GAME_WIDTH = 600
GAME_HEIGHT = 400
SNAKE_SIZE = 10
INITIAL_SNAKE_SPEED = 100  # Lower is faster
SNAKE_COLOR = "green"
FOOD_COLOR = "red"
BACKGROUND_COLOR = "black"

# Directions
DIRECTIONS = {"Left": (-SNAKE_SIZE, 0), "Right": (SNAKE_SIZE, 0), "Up": (0, -SNAKE_SIZE), "Down": (0, SNAKE_SIZE)}

# Initialize the game window
def initialize_window():
    root = tk.Tk()
    root.title("Snake Game")
    root.resizable(False, False)
    canvas = tk.Canvas(root, width=GAME_WIDTH, height=GAME_HEIGHT, bg=BACKGROUND_COLOR)
    canvas.pack()
    return root, canvas

def initialize_game():
    # Initialize snake in the center and create the first piece of food
    snake = [(GAME_WIDTH // 2, GAME_HEIGHT // 2)]
    current_direction = "Right"
    food = place_food()
    score = 0
    return {"snake": snake, "direction": current_direction, "food": food, "score": score, "game_over": False}

def place_food():
    """Places food at a new random location."""
    return (random.randint(0, (GAME_WIDTH // SNAKE_SIZE) - 1) * SNAKE_SIZE, 
            random.randint(0, (GAME_HEIGHT // SNAKE_SIZE) - 1) * SNAKE_SIZE)

def update_canvas(canvas, game_state):
    """Updates the canvas by drawing the snake and food."""
    canvas.delete("all")
    snake, food = game_state["snake"], game_state["food"]
    
    # Draw the snake
    for (x, y) in snake:
        canvas.create_rectangle(x, y, x + SNAKE_SIZE, y + SNAKE_SIZE, fill=SNAKE_COLOR)
    
    # Draw the food
    food_x, food_y = food
    canvas.create_rectangle(food_x, food_y, food_x + SNAKE_SIZE, food_y + SNAKE_SIZE, fill=FOOD_COLOR)
    
    # Draw the score
    canvas.create_text(10, 10, anchor='nw', font=('ComicSans', 16), text=f'Score: {game_state["score"]}', fill='white')

def move_snake(game_state):
    """Moves the snake based on its current direction and updates the game state."""
    snake, direction, food, score, game_over = (game_state["snake"], game_state["direction"], 
                                                game_state["food"], game_state["score"], game_state["game_over"])
    
    if game_over:
        return game_state  # Don't update if the game is over

    # Calculate new head position
    head_x, head_y = snake[0]
    move_x, move_y = DIRECTIONS[direction]
    new_head = (head_x + move_x, head_y + move_y)

    # Check for collision with walls
    if new_head[0] < 0 or new_head[0] >= GAME_WIDTH or new_head[1] < 0 or new_head[1] >= GAME_HEIGHT:
        game_state["game_over"] = True
        return game_state

    # Check for collision with self
    if new_head in snake:
        game_state["game_over"] = True
        return game_state

    # Insert new head
    new_snake = [new_head] + snake[:-1]

    # Check if the snake has eaten the food
    if new_head == food:
        score += 1
        new_snake.append(snake[-1])  # Grow the snake
        food = place_food()  # Place new food

    game_state.update({"snake": new_snake, "food": food, "score": score})
    return game_state

def change_direction(event, game_state):
    """Updates the direction in the game state based on the player's input."""
    new_direction = event.keysym
    current_direction = game_state["direction"]
    
    # Prevent the snake from reversing direction
    if (new_direction == "Left" and current_direction != "Right") or \
       (new_direction == "Right" and current_direction != "Left") or \
       (new_direction == "Up" and current_direction != "Down") or \
       (new_direction == "Down" and current_direction != "Up"):
        game_state["direction"] = new_direction
    
    return game_state

def game_loop(root, canvas, game_state):
    """Main game loop to keep updating the snake's movement."""
    if game_state["game_over"]:
        canvas.create_text(GAME_WIDTH // 2, GAME_HEIGHT // 2, text="Game Over", font=('Arial', 24), fill='red')
    else:
        # Update snake movement and redraw
        game_state = move_snake(game_state)
        update_canvas(canvas, game_state)
        root.after(INITIAL_SNAKE_SPEED, lambda: game_loop(root, canvas, game_state))

def start_game():
    """Starts the game, sets up the window, and runs the main loop."""
    root, canvas = initialize_window()
    game_state = initialize_game()
    
    # Bind keys to change snake direction
    root.bind("<Left>", lambda event: change_direction(event, game_state))
    root.bind("<Right>", lambda event: change_direction(event, game_state))
    root.bind("<Up>", lambda event: change_direction(event, game_state))
    root.bind("<Down>", lambda event: change_direction(event, game_state))
    
    # Start the game loop
    game_loop(root, canvas, game_state)
    
    # Start the Tkinter main loop
    root.mainloop()

# Run the game
start_game()
