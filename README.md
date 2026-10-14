# Cosmic Sudoku 🌌

A Sudoku game with a Python (Flask) backend and a JavaScript frontend.

## Features

- Randomly generated puzzles (Easy / Medium / Hard)
- Backtracking solver written in Python
- Mistake counter, timer, and win detection
- Start screen and New Game button

## Project structure

    sudoku/
    ├── backend/
    │   ├── app.py          # Flask API
    │   ├── sudoku.py       # Rules and solver
    │   └── generator.py    # Puzzle generator
    ├── index.html
    ├── style.css
    └── script.js

## How to run

1. Install dependencies: `pip install flask flask-cors`
2. Start the server: `python backend/app.py`
3. Open `index.html` in your browser and press Play.