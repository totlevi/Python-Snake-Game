import pygame
import time
import random

# Initialize pygame
pygame.init()

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Define screen size
screen_width = 800
screen_height = 600

# Create the game window
game_window = pygame.display.set_mode((screen_width, screen_height))

# Set the window title
pygame.display.set_caption("Snake Game")

# Define font size and font style
font_size = 30
font_style = pygame.font.SysFont(None, font_size)

# Define function to display message on screen
def message(msg, color):
    message_text = font_style.render(msg, True, color)
    game_window.blit(message_text, [screen_width/6, screen_height/3])

# Define function to display score on screen
def show_score(score):
    score_text = font_style.render("Score: " + str(score), True, black)
    game_window.blit(score_text, [0, 0])

# Define function to draw the snake
def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(game_window, black, [x[0], x[1], snake_block, snake_block])

# Define the game loop function
def game_loop():
    game_over = False
    game_close = False

    # Set the initial position of the snake
    x1 = screen_width / 2
    y1 = screen_height / 2

    # Set the change in position of the snake
    x1_change = 0       
    y1_change = 0

    # Define the size of the snake blocks
    snake_block = 10

    # Define the initial length of the snake
    snake_list = []
    Length_of_snake = 1

    # Define the location of the food
    food_x = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0

    # Game loop
    while not game_over:

        # Display a message if the game is over
        while game_close == True:
            game_window.fill(white)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            show_score(Length_of_snake - 1)
            pygame.display.update()

            # Wait for user to choose an option
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        # Update the position of the snake
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
        # Update the position of the snake head
        x1 += x1_change
        y1 += y1_change

        # Check if the snake hit the boundary
        if x1 >= screen_width or x1 < 0 or y1 >= screen_height or y1 < 0:
            game_close = True

        # Update the position of the food and snake length if the snake ate the food
        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
            food_y = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        # Create the snake head and body
        game_window.fill(white)
        pygame.draw.rect(game_window, red, [food_x, food_y, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_list.append(snake_Head)
        if len(snake_list) > Length_of_snake:
            del snake_list[0]

        # Check if the snake hit its own body
        for x in snake_list[:-1]:
            if x == snake_Head:
                game_close = True

        # Draw the snake and display the score
        draw_snake(snake_block, snake_list)
        show_score(Length_of_snake - 1)
        pygame.display.update()

        # Set the speed of the game
        pygame.time.delay(30)

    # Quit pygame and exit the program
    pygame.quit()
    quit()

# Start the game loop
game_loop()