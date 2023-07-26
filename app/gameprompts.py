"""gameprompts.py
"""

from app.bcolors import BColors


class GamePrompts:
    @staticmethod
    def choose_game_type() -> str:
        """Allows the user to choose between the two game types: words or phrases.

        Returns:
            str: user choice
        """

        options = ["p", "w"]
        while True:
            choice = input("Choose game type: w for words, p for phrases: ").lower()[0]
            if (not choice.isalpha()) or (choice not in options):
                print("Your choice is not in the list of options")
                BColors.warning("That's not one of the options available. Try again.")
                continue
            break
        return choice

    @staticmethod
    def get_username() -> str:
        """Prompts the user for a username and returns it.

        Returns:
            str: username
        """
        name = input("What's your name? ")
        return name

    @staticmethod
    def choose_difficulty() -> str:
        """Return the difficulty chosen by the user: easy, medium and hard word lists.

        Returns:
            str: choice
        """

        options = ["e", "m", "h"]
        while True:
            choice = input(
                "Choose difficulty: e for easy. n for normal. h for hard. "
            ).lower()[0]
            if (not choice.isalpha()) or (choice not in options):
                BColors.warning("That's not one of the options available. Try again.")
                continue
            break
        return choice

    @staticmethod
    def choose_topic():
        """Return the topic of the phrases for a phrase; currently limited to idioms or slogans

        Return:
            str: topic chosen
        """

        options = ["i", "s"]
        while True:
            choice = input("Choose difficulty: i for idioms. s for slogans: ").lower()[
                0
            ]
            if (not choice.isalpha()) or (choice not in options):
                BColors.warning("That's not one of the options available. Try again.")
                continue
            break
        return choice
