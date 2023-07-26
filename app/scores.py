"""scores.py
"""
import json


class Scores:
    SCORES_FILENAME = "highscores.json"

    def __init__(self, username: str) -> None:
        self._scores = self.load_scores()
        self.username = username

    @property
    def scores(self):
        return self._scores

    @scores.setter
    def scores(self, new_scores: dict):
        self._scores = new_scores

    def load_scores(self):
        """Loads and returns a json containing the user's high scores.

        Returns:
            str: json
        """

        with open(self.SCORES_FILENAME) as f:
            return json.load(f)

    def save_scores(self, new_wins: int):
        """Saves the high score of the current user."""

        current_score = new_wins
        old_score = self.scores.get(self.username)

        if old_score is None or current_score > old_score:
            self.high_scores[self.username] = current_score
            with open(self.SCORES_FILENAME, "w") as f:
                json.dump(self.high_scores, f, indent=6)
