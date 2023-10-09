# Tic Tac Toe Game with AI and Player vs Player

This is a simple implementation of the classic Tic Tac Toe game using Python and the Pygame library. The game supports two levels of AI and allows for player vs player mode.

## Game Description

Tic Tac Toe is a classic paper-and-pencil game where two players, represented by "X" and "O", take turns to mark a 3x3 grid. The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row wins the game.

## Table of Contents
 - Installation
 - Usage
 - Game Modes
 - AI Levels
 - AI Algorithm: Minimax
 - Controls
 - Credits
 - License

## Installation
Make sure you have Python installed. If not, you can download it from [Python's official website.](https://pip.pypa.io/en/stable/)

Install the required packages using pip:

```bash
pip install pygame
```
Clone this repository or download the source code to your local machine.

## Usage
Run the game by executing the Main_menu.py file:
```bash
python Main_menu.py
```
## Game Modes
Player vs Player (PvP): Two human players take turns to play the game.\
Player vs AI (PvAI): A human player plays against the AI.

## AI Levels
>The AI comes with two levels of difficulty:\
>Random AI (Level 0): The AI makes random moves on the board.\
>Minimax AI (Level 1): The AI uses the minimax algorithm to choose the best moves.

## AI Algorithm: Minimax
>The Minimax algorithm is a decision-making algorithm used in two-player games like Tic Tac Toe. It evaluates all possible game states resulting from each possible move and chooses the best move for the AI, assuming the opponent also plays optimally. The algorithm aims to minimize the possible loss for a worst-case scenario while maximizing its potential gain.

## Controls
Mouse Click: Place your marker in an empty cell by clicking on it.\
R Key: Restart the game.

## Screenshots

![Screenshot 1](https://github.com/SOHAMRANA77/tic-tac-toe/blob/a1b728f390db9f8b0f716a3e843faae2675620f3/img/Screenshot%202023-10-09%20133250.png)

>In this screenshot, we see a game of Tic Tac Toe in progress. The game is played on a 3x3 grid, where two players take turns marking the cells with their respective symbols, "X" and "O". The player with the "X" symbol is the first to move, followed by the player with the "O" symbol.
The grid is divided into nine squares, and to make a move, a player simply clicks on an empty square to place their symbol. The objective of the game is to be the first to achieve three of their symbols in a horizontal, vertical, or diagonal row. When a win condition is met, the winning line is highlighted, indicating the winning move.
At the top or side of the grid, there is typically a display showing which player's turn it is (either "Player X" or "Player O"). Additionally, there might be a reset button to start a new game.
The game is easy to play and understand, making it a popular choice for quick and enjoyable entertainment.
Replace screenshot_link with the actual link to the Tic Tac Toe game screenshot. Feel free to add more specific details about the screenshot if needed.


## License

This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/)
