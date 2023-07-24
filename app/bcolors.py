"""bcolors.py
"""


class BColors:
    """CLI colors and associated functions"""

    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"

    @staticmethod
    def warning(text: str):
        print(f"{BColors.WARNING}{text}{BColors.ENDC}")

    @staticmethod
    def failure(text: str):
        print(f"{BColors.FAIL}{text}{BColors.ENDC}")

    @staticmethod
    def header(text: str):
        print(f"{BColors.HEADER}{text}{BColors.ENDC}")

    @staticmethod
    def underline(text: str):
        print(f"{BColors.UNDERLINE}{text}{BColors.ENDC}")

    @staticmethod
    def blue(text: str):
        print(f"{BColors.OKBLUE}{text}{BColors.ENDC}")

    @staticmethod
    def green(text: str):
        print(f"{BColors.OKGREEN}{text}{BColors.ENDC}")

    @staticmethod
    def bold(text: str):
        print(f"{BColors.BOLD}{text}{BColors.ENDC}")


if __name__ == "__main__":
    pass
