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
>The AI comes with two levels of difficulty:
>Random AI (Level 0): The AI makes random moves on the board.
>Minimax AI (Level 1): The AI uses the minimax algorithm to choose the best moves.

## AI Algorithm: Minimax
>The Minimax algorithm is a decision-making algorithm used in two-player games like Tic Tac Toe. It evaluates all possible game states resulting from each possible move and chooses the best move for the AI, assuming the opponent also plays optimally. The algorithm aims to minimize the possible loss for a worst-case scenario while maximizing its potential gain.

## Controls
Mouse Click: Place your marker in an empty cell by clicking on it.\
R Key: Restart the game.

## License

This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/)
