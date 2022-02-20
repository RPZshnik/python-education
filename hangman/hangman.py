"""
This module implements the Hangman game.

"""

import os
import random
import sys
from getpass import getpass

WORDS_FILE = "./words.txt"


class Hangman:
    """
    This is a class that implements Hangman game logic.

    """
    def __init__(self, attempts=6):
        self.word = ""
        self.public_word = []
        self.attempts = attempts
        self.attempts_left = self.attempts
        self.used_letters = []
        self.wildcard = "_"

    def input_of_word(self):
        """
        This function for input the game word.
        :return:
        """
        self.word = getpass("Enter the world: ")

    def save_word(self):
        """
        Function to save used word.
        :return:
        """
        try:
            os.makedirs(WORDS_FILE)
        except FileExistsError:
            pass
        finally:
            with open(WORDS_FILE, "a", encoding="utf-8") as file:
                file.seek(0)
                file.write(f"{self.word}\n")

    def print_stats(self):
        """
        This function print state of game.
        :return:
        """
        print("Word ", " ".join(self.public_word))
        print("Used letters: ", ", ".join(self.used_letters))
        print(f"Attempts left: {self.attempts_left}/{self.attempts}", end="\n\n")

    def check_letter(self, letter: str):
        """
        This function check user input letter.
        :param letter:
        :return:
        """
        for index, _ in enumerate(self.word):
            if self.word[index] == letter:
                self.public_word[index] = letter.upper()
        self.used_letters.append(letter)

    def open_initial_letters(self):
        """
        This function defines amount of necessary letter and open them to the player.
        :return:
        """
        amount_of_letters = int(len(self.word) * 0.2)
        while len(self.public_word) - self.public_word.count(self.wildcard) < amount_of_letters:
            index = random.randint(0, len(self.word) - 1)
            self.public_word[index] = self.word[index]

    def answer_input(self, message):
        """

        :param message: Message for user
        :return: Returns True if the player was able to guess the word otherwise False
        """
        word = input(message)
        return word.upper() == self.word.upper()

    def letter_input(self):
        """
        Function that implement input of player letter
        :return: Return player letter
        """
        letter = input("Enter letter (press enter to write a word): ")
        if letter == "":
            return ""
        while letter in self.used_letters:
            print("This letter was used.")
            letter = input("Enter letter again: ")
        return letter

    def start_game(self):
        """
        This function start the game.
        :return:
        """
        self.input_of_word()
        self.public_word = [self.wildcard] * len(self.word)
        self.open_initial_letters()
        self.save_word()
        self.print_stats()
        while self.attempts_left > 0:
            letter = self.letter_input()
            self.attempts_left -= 1
            if letter == "":
                return self.answer_input("Enter the word: ")
            else:
                self.check_letter(letter)
            if self.wildcard not in self.public_word:
                return True
            self.print_stats()
        return self.answer_input("Attempt is over, enter a word: ")


def choose_action():
    """
    This function implements a game menu with choice.
    :return:
    """
    print("Choose an action: ")
    print("Start game - 1")
    print("Previous words - 2")
    print("Exit - 3", end="\n\n")
    action = int(input("Your choice: "))
    print()
    return action


def print_previous_words(limit: int):
    """
    This function print list of previous game words.
    :param limit: The value on which depends number of output words.
    :return:
    """
    with open(WORDS_FILE, "r", encoding="utf-8") as file:
        for word in file.readlines()[-limit:]:
            print(word, end="")
    print()


def game_main_loop():
    """
    Game main loop function
    :return:
    """
    action = choose_action()
    if action == 1:
        game = Hangman()
        can_guess = game.start_game()
        if can_guess:
            print("Congratulations!!! You were able to guess the word.", end="\n\n")
        else:
            print("Unfortunately the attempt is over.")
    elif action == 2:
        amount_of_words = input("Enter amount of words (default: the whole list): ")
        print_previous_words(int(amount_of_words) if amount_of_words else 0)
    elif action == 3:
        sys.exit()


def main():
    """
    Main function with infinity loop.
    :return:
    """
    while True:
        game_main_loop()


if __name__ == "__main__":
    main()
