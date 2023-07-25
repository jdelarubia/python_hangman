"""game.py
"""
import random
import sys
import json
from app.bcolors import BColors
from app.gameprompts import GamePrompts


class Game:
    def __init__(self):
        self.chances = 6
        self.high_scores = {}
        self.missed = []
        self.discovered = []
        self.display = ""
        self.username = ""
        self.wins = 0
        self.losses = 0

        self.load_highscore()
        self.get_username()


    def get_username(self):
        """Allows the user to choose a username"""
        name = GamePrompts.get_username()
        message = (
            f"Welcome back, {name}"
            if self.high_scores.get(name)
            else f"Nice to meet you, {name}"
        )
        print(message)
        print("I'll be keeping track of your high score. Good Luck!\n")
        self.username = name


    @staticmethod
    def choose_topic():
        """
        Allows the user to choose the topic of the phrases for a phrase. There are currently
        options to choose idioms or slogans

        :return:
        """

        options = ["i", "I", "s", "S"]

        while True:
            choice = input("Choose difficulty: i for idioms. s for slogans: ")
            if choice.isalpha():
                if len(choice) == 1:
                    if choice in options:
                        choice = choice.lower()
                        break
                    else:
                        BColors.warning(
                            "That's not one of the options I gave you. Try again."
                        )
                else:
                    BColors.warning("I only need one letter. Try again.")
            else:
                BColors.warning("Letters only, please. Try again.")

        return choice

    @staticmethod
    def word_game_setup(difficulty):
        """
        Set up game by choosing the target word from a file based on difficulty

        :param difficulty:
        :return:
        """

        filename_map = {
            "e": "easy_hang_words.txt",
            "n": "normal_hang_words.txt",
            "h": "hang_words.txt",
        }

        filename = filename_map.get(difficulty, "easy_hang_words.txt")

        with open(filename, "r") as open_file:
            all_text = open_file.read()

        word_list = all_text.split("\n")
        target = random.choice(word_list)

        return target

    @staticmethod
    def phrase_game_setup(topic):
        """
        Set up game by choosing the target phrase from a file based on topic

        :param topic:
        :return:
        """

        d = {"i": "idioms.txt", "s": "slogans.txt"}

        with open(d[topic], "r") as open_file:
            all_text = open_file.read()

        phrase_list = all_text.split("\n")
        target = phrase_list[random.randrange(0, len(phrase_list))]
        target = target.lower()
        return target

    def guess(self, targeted, game_type):
        """
        Asks the user to submit a letter guess, then validates the input,
        shows the letters they missed or reveals the word with the letters
        they correctly guessed.

        :param targeted:
        :param game_type:
        :return:
        """

        correct_guess_text = [
            "You guessed it!",
            "Nice job!",
            "That's right!",
            "I see what you did there.",
            "Keep it up!",
            "Just a few more to go!",
        ]
        target = targeted
        self.display = ""

        guess = input("Guess a letter or type 'solve': ")

        if guess.isalpha():
            if len(guess) == 1:
                guess = guess.lower()
                if guess in self.discovered:
                    BColors.warning("You already guessed that. Try again.")
                elif guess in target:
                    self.discovered.append(guess)
                    print(
                        correct_guess_text[random.randrange(0, len(correct_guess_text))]
                    )
                else:
                    if guess not in self.missed:
                        self.missed.append(guess)
                        print("That's not right. Try again.")
                        self.chances -= 1
                    else:
                        BColors.warning("You already guessed that. Try again.")
                print("Missed Letters: ", self.missed)
            elif guess in ["solve", "exit", "quit"]:
                if guess == "solve":
                    if game_type == "p":
                        solution = input("Enter the full phrase: ")
                    else:
                        solution = input("Enter the full word: ")
                    result = "win" if solution == target else "lose"
                    self.win_lose(result, game_type, target)
                else:
                    print("Thanks for playing")
                    sys.exit()
            else:
                BColors.warning("You can only guess one letter at a time.")
        else:
            BColors.warning("Try guessing a letter")

        self.display = ""
        for n in target:
            self.display += (
                (n + " ") if n in self.discovered else (" / " if n == " " else "_ ")
            )
        print(self.display)

    def play(self):
        """
        Starts the game, reviews the guessing progress and shares the victory or defeat message

        :return:
        """

        wants_to_play = True
        while wants_to_play:
            self.chances = 6
            game_type = GamePrompts.choose_game_type()
            if game_type == "w":
                difficulty = GamePrompts.choose_difficulty()
                target = self.word_game_setup(difficulty)
            elif game_type == "p":
                topic = self.choose_topic()
                target = self.phrase_game_setup(topic)
            else:
                raise Exception("How did this even happen?")
            challenge = ""
            for letter in target:
                challenge += " / " if letter == " " else "_ "
            print("Alright, let's get started. Can you solve this? : \n")
            print(challenge)
            while self.chances > 0:
                self.guess(target, game_type)
                print(f"You have {self.chances} guesses remaining.")
                print()
                target_words = self.display.split("/")
                current_guess = "".join(word.replace(" ", "") for word in target_words)
                if current_guess == target:
                    self.win_lose("win", game_type, target)
                    wants_to_play = self.play_again()
                    break
            else:
                self.win_lose("loss", game_type, target)
                wants_to_play = self.play_again()

    def win_lose(self, result, game_type, target):
        """
        Print the win/loss result.

        :param result:
        :param game_type:
        :param target:
        :return:
        """

        message = ""
        if result == "win":
            BColors.green("You win!")
            self.wins += 1
            message = f"You've won {self.wins} time{'s' if self.wins != 1 else ''}"
        elif result == "loss":
            BColors.failure("Game Over! You Lose")
            self.losses += 1
            message = f"You've lost {self.losses} time{'s' if self.losses != 1 else ''}"

        print(f"The correct {'phrase' if game_type == 'p' else 'word'} was: {target}")
        print(message)

    def play_again(self):
        """
        Ask whether the user would like to play again
        :return:
        """

        self.save_highscore()
        again = input("Wanna play again? Y/N: ")
        if again.lower() == "y":
            print("Yay! Let's go again" + "\n")
            self.reset_values()
            return True
        else:
            print("Thanks for playing!")
            rounds = self.wins + self.losses
            percent = (float(self.wins) / rounds) * 100
            print(f"You played {rounds} times")
            print(f"You won {percent:.1f}% of games!")
            return False

    def reset_values(self):
        """
        Resets global game value variables

        :return:
        """

        self.chances = 6
        self.missed = []
        self.discovered = []
        self.display = ""

    def save_highscore(self):
        """
        Saves the high score of the current user

        :return:
        """

        current_score = self.wins
        old_score = self.high_scores.get(self.username)

        if old_score is None or current_score > old_score:
            self.high_scores[self.username] = current_score
            with open("highscores.json", "w") as f:
                json.dump(self.high_scores, f, indent=6)

    def load_highscore(self):
        """
        Load the high scores

        :return:
        """

        with open("highscores.json") as f:
            self.high_scores = json.load(f)
