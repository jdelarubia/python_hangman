""" A revised game of hangman with two game modes. You can guess words at 3
difficulty levels or guess a common phrase. In each mode you only have 6
chances to guess the right letter. You also have the option to play again. """

from app.game import Game
from app.gameprompts import GamePrompts
from app.scores import Scores


def welcome_user():
    print("Welcome to Hang_words.")
    print(
        "You can quit the game by typing 'exit' or 'quit' instead of guessing a letter. "
    )
    print()


def greet_user(username: str, scores: dict):
    message = (
        f"Welcome back, {username}"
        if scores.get(username)
        else f"Nice to meet you, {username}"
    )
    print(message)
    print("I'll be keeping track of your high score. Good Luck!\n")


if __name__ == "__main__":
    """
    The action starts here
    """
    welcome_user()
    username = GamePrompts.get_username()
    scores = Scores(username=username)
    greet_user(username=username, scores=scores.scores)
    g = Game(username, scores)
    g.play()
