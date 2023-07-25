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

