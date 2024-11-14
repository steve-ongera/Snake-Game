import pygame
import time
import random

pygame.init()

# Define colors
white = (255, 255, 255)
yellow = (255, 255, 102)
blue = (50, 153, 255)
pink = (255, 105, 180)
purple = (128, 0, 128)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)

# Set display width and height
dis_width = 600
dis_height = 400

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()

snake_block = 10
initial_snake_speed = 5  # Slower initial speed
speed_increase = 1  # Speed increment per fruit eaten
snake_speed = initial_snake_speed  # Declare it here to avoid the UnboundLocalError

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Function to display score
def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, white)  # Score in white
    dis.blit(value, [0, 0])

# Function to draw snake
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])

# Function to display message
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

# Function to randomly select a color and corresponding score
def random_food():
    food_color = random.choice([blue, pink, purple, yellow])
    if food_color == blue:
        score_value = 5
    elif food_color == pink:
        score_value = 4
    elif food_color == purple:
        score_value = 3
    elif food_color == yellow:
        score_value = 1
    return food_color, score_value

# Main function for the game
def gameLoop():
    global snake_speed  # Add this line to indicate that we're using the global variable
    
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    # Set the initial food
    foodx, foody = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0, round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
    food_color, food_score = random_food()  # Get the color and score for the fruit

    while not game_over:

        while game_close == True:
            dis.fill(black)  # Set background to black
            message("You Lost! Press Q-Quit or C-Play Again", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

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

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(black)  # Set background to black

        # Draw the fruit with the randomly selected color
        pygame.draw.rect(dis, food_color, [foodx, foody, snake_block, snake_block])
        
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)  # Display score on screen

        pygame.display.update()

        # Check if the snake eats the fruit
        if x1 == foodx and y1 == foody:
            foodx, foody = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0, round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            food_color, food_score = random_food()  # Get new food color and score value
            Length_of_snake += 1
            snake_speed += speed_increase  # Increase snake speed after eating food

        clock.tick(snake_speed)  # Control the snake speed

    pygame.quit()
    quit()

gameLoop()
