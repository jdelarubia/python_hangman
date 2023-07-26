"""loaders.py
"""

import random


class WordLoader:
    file_mapper = {
        "e": "easy_hang_words.txt",
        "n": "normal_hang_words.txt",
        "h": "hang_words.txt",
    }

    @staticmethod
    def get_random_word(difficuly_level: str) -> str:
        default = WordLoader.file_mapper["e"]
        filename = WordLoader.file_mapper.get(difficuly_level, default)
        with open(filename, "r") as words_file:
            all_words = words_file.read().split("\n")

        return random.choice(all_words)


class PhraseLoader:
    file_mapper = {
        "i": "idioms.txt",
        "s": "slogans.txt",
    }

    @staticmethod
    def get_random_phrase(topic: str) -> str:
        default = PhraseLoader.file_mapper["i"]
        filename = PhraseLoader.file_mapper.get(topic, default)
        with open(filename, "r") as phrases_file:
            all_phrases = phrases_file.read().split("\n")

        return random.choice(all_phrases)
