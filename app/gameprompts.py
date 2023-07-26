"""gameprompts.py
"""

from app.bcolors import BColors


class GamePrompts:
    @staticmethod
    def get_choice_from_user(prompt: str, choices: list) -> str:
        """Given a prompt to show the user and a list of possible choices, return a single choice

        Args:
            prompt (str): message to be shown on screen
            choices (list): list of choices available

        Returns:
            str: choice
        """
        while True:
            choice = input(prompt).lower()[0]
            if (not choice.isalpha()) or (choice not in choices):
                print("Your choice is not in the list of options")
                BColors.warning("That's not one of the options available. Try again.")
                continue
            break
        return choice

    @staticmethod
    def choose_game_type() -> str:
        """Allows the user to choose between the two game types: words or phrases.

        Returns:
            str: user choice
        """
        choices = ["p", "w"]
        prompt = "Choose game type: w for words, p for phrases: "
        return GamePrompts.get_choice_from_user(prompt, choices)

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
        choices = ["e", "m", "h"]
        prompt = "Choose difficulty: e for easy. n for normal. h for hard. "
        return GamePrompts.get_choice_from_user(prompt, choices)

    @staticmethod
    def choose_topic():
        """Return the topic of the phrases for a phrase; currently limited to idioms or slogans

        Return:
            str: topic chosen
        """
        choices = ["i", "s"]
        prompt = "Choose difficulty: i for idioms. s for slogans: "
        return GamePrompts.get_choice_from_user(prompt, choices)
