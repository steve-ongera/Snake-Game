# Snake Game

This is a classic Snake game implemented using Python and the `pygame` library. The game features dynamic speed adjustments, random-colored fruits with different scores, and a scoring system to track the player's performance.

## Features

- **Snake Movement**: The snake can move up, down, left, and right.
- **Speed Increase**: The snake's speed increases slightly each time it eats a fruit.
- **Fruit Types**: The fruits are randomly assigned one of four colors, each associated with a different score:
  - **Blue** fruit = 5 points
  - **Pink** fruit = 4 points
  - **Purple** fruit = 3 points
  - **Yellow** fruit = 1 point
- **Score Display**: The score is updated in real-time at the top left of the screen.
- **Game Over**: The game ends if the snake collides with the screen edges or itself.

## Requirements

Before running the game, make sure you have the following software installed:

- Python 3.x (preferably Python 3.6 or higher)
- `pygame` library

To install `pygame`, run the following command:


`pip install pygame`


## Installation
Clone or download this repository to your local machine.

Install the necessary dependencies (pygame).

Open the project folder and run the game with the following command:


python snake.py

## Controls

- Arrow Keys: Use the arrow keys on your keyboard to control the snake:
- Left Arrow: Move Left
- Right Arrow: Move Right
- Up Arrow: Move Up
- Down Arrow: Move Down
- Q: Quit the game after losing.
- C: Play again after losing.

## Game Instructions

- Starting the Game: When you start the game, the snake will appear in the center of the screen, and a random fruit will appear at a random location.

- Eating Fruits: The snake grows each time it eats a fruit, and the game score is updated. The snake's speed increases slightly after each fruit.

- Game Over: The game ends when the snake collides with the edges of the screen or itself. After the game ends, you will have the option to quit the game (press Q) or play again (press C).

- Score: The current score is displayed at the top left of the screen and increases based on the type of fruit consumed.

## Code Overview
**Variables:**

dis_width, dis_height: Defines the dimensions of the game window (600x400).

- snake_block: Size of each segment of the snake (10 pixels).
- initial_snake_speed: The initial speed of the snake when the game starts.
- snake_speed: Current speed of the snake, which increases as the snake eats more fruits.
- snake_List: Stores the snake's body as it grows.
- Length_of_snake: Keeps track of the current length of the snake.
- food_color, food_score: The color and score of the fruit.

## Functions:
- Your_score(score): Displays the current score at the top left of the screen.
- our_snake(snake_block, snake_list): Draws the snake on the screen based on its current position.
- message(msg, color): Displays a message (e.g., game over or instructions) in a specific color.
- random_food(): Generates a random fruit color and returns the corresponding score value.
- gameLoop(): Main game logic where the snake moves, eats fruits, and the game checks for collisions.

## Key Logic:
- Movement: The snake moves based on the arrow key pressed.
- Fruit Generation: Fruits are placed at random locations with a randomly assigned color and score.
- Speed Increase: After each fruit is eaten, the snake’s speed increases slightly.
- Game Over: The game ends if the snake hits the screen borders or itself.

## License
This project is open source and available under the MIT License.

## Acknowledgements
This project was created as a learning exercise in Python and pygame.
The original Snake game concept was developed in 1976 by Gremlin, and has been a popular game in various forms ever since.

 **Feel free to modify and extend this project as needed. Enjoy the game!**

 
### Key Sections:

1. **Introduction**: Describes the project and its features.
2. **Requirements**: Lists the dependencies and how to install them (`pygame`).
3. **Installation**: Instructions to get the project up and running.
4. **Controls**: Lists the key controls used to play the game.
5. **Game Instructions**: Describes how to play the game, what happens during gameplay, and the mechanics of the snake and scoring system.
6. **Code Overview**: Explains the structure and key functions of the code.
7. **License and Acknowledgments**: Mentions the license and credits.

### Usage:

This `README.md` should help users understand the functionality and usage of your Snake game. Let me know if you need more details or changes!

