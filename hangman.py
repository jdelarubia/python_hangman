""" A revised game of hangman with two game modes. You can guess words at 3
difficulty levels or guess a common phrase. In each mode you only have 6
chances to guess the right letter. You also have the option to play again. """

from app.bcolors import BColors
from app.game import Game


if __name__ == "__main__":
    """
    The action starts here
    """
    print("Welcome to Hang_words.")
    print(
        "You can quit the game by typing 'exit' or 'quit' instead of guessing a letter. "
    )
    print()
    g = Game()
    g.play()
