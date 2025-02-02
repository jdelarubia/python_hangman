"""game.py
"""
import random
import sys
from app.bcolors import BColors
from app.gameprompts import GamePrompts
from app.scores import Scores
from app.loaders import WordLoader, PhraseLoader


class Game:
    def __init__(self, username: str, scores: Scores):
        self.username = username
        self.scores = scores
        self.high_scores = scores.scores
        self.wins = 0
        self.losses = 0
        self.reset_values()

    @staticmethod
    def word_game_setup(difficulty):
        """
        Set up game by choosing the target word from a file based on difficulty

        :param difficulty:
        :return:
        """
        return WordLoader.get_random_word(difficuly_level=difficulty)

    @staticmethod
    def phrase_game_setup(topic):
        """
        Set up game by choosing the target phrase from a file based on topic

        :param topic:
        :return:
        """
        return PhraseLoader.get_random_word(topic=topic)

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
                print("Missed Letters: ", sorted(self.missed))
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
                topic = GamePrompts.choose_topic()
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

        self.scores.save_scores(self.wins)
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
