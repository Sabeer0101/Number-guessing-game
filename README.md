# 🎯 Number Guessing Game

A simple command-line game built with **Python**. The computer picks a secret number and you try to guess it in limited attempts.

## ✨ Features

- 3 difficulty levels (Easy, Medium, Hard)
- "Too high / too low" feedback after every guess
- Hint (odd/even) when you are down to your last attempts
- Score based on how fast you guess
- High score saved in a file, so it stays even after you close the game
- Input validation (no crash on wrong input)

## 🛠️ Tech Used

![Python](https://img.shields.io/badge/Python-10A37F?style=flat-square&logo=python&logoColor=white)

Concepts practiced: loops, functions, conditionals, `random` module, file handling, error handling.

## 🚀 How to Run

1. Install [Python 3](https://www.python.org/downloads/)
2. Clone this repo
   ```bash
   git clone https://github.com/Sabeer0101/number-guessing-game.git
   cd number-guessing-game
   ```
3. Run the game
   ```bash
   python guessing_game.py
   ```

## 🎮 Sample Output

```
========================================
   WELCOME TO NUMBER GUESSING GAME
========================================

Select difficulty:
  1. Easy  (1 to 50, 10 attempts)
  2. Medium  (1 to 100, 7 attempts)
  3. Hard  (1 to 500, 9 attempts)
Enter choice (1/2/3): 2

I'm thinking of a number between 1 and 100.
You have 7 attempts. Good luck!

Attempt 1/7
Your guess: 50
Too low! Try a bigger number.
```

## 🔮 Future Improvements

- [ ] Multiplayer mode (2 players)
- [ ] Leaderboard with player names
- [ ] GUI version using Tkinter

## 👨‍💻 Author

**Sabeer** — [GitHub](https://github.com/Sabeer0101)
