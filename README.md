# Higher or Lower Game

A fun and interactive game where players guess which of two options has a higher number of social media followers. Test your knowledge of celebrity and brand popularity in this engaging game.

---

## Table of Contents
- [Features](#features)
- [Setup](#setup)
- [How to Play](#how-to-play)
- [Code Structure](#code-structure)
- [Future Improvements](#future-improvements)

---

## Features
- **Dynamic Data**: Includes a wide variety of celebrities, brands, and public figures.
- **Score Tracking**: Keeps track of the player’s score.
- **Randomized Gameplay**: Ensures each round presents a new challenge by randomizing the options.
- **Interactive Gameplay**: Provides real-time feedback on guesses.

---

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/ryangsling/Higher-or-Lower-game.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Higher-or-Lower-game
   ```

3. Run the game using Python:
   ```bash
   python main.py
   ```

---

## How to Play
1. The game will display two options, `A` and `B`, with details about each, such as name, description, and country.
2. Guess which option has more followers by typing `A` or `B`.
3. If your guess is correct, your score increases, and the game continues with a new pair.
4. If your guess is wrong, the game ends, and your final score is displayed.

---

## Code Structure

### `main.py`
Handles the main game logic, including:
- Displaying the options.
- Accepting user input.
- Determining correctness of answers.

### `logo_and_data.py`
- Contains the data for the game, including names, follower counts, descriptions, and countries.
- Includes ASCII art for the game logo and comparison graphic.

### Example Data Entry
```python
{
    'name': 'Cristiano Ronaldo',
    'follower_count': 643,
    'description': 'Footballer',
    'country': 'Portugal'
}
```

---

## Future Improvements
- Will add more data for greater variety.
- Will Implement difficulty levels.
- Will try to Create a graphical user interface (GUI) for better visual appeal.
- Will Add a leaderboard to display high scores.

---

Enjoy the game and test your knowledge! Feel free to contribute by opening issues or pull requests on GitHub.

