import string
from functools import total_ordering


@total_ordering
class Contrived:

    def __init__(self, letter, number):
        Contrived._validate_letter(letter)
        Contrived._validate_number(number)

        self.letter = letter
        self.number = number

    def sum(self):
        return ord(self.letter) + self.number

    def __str__(self):
        return f"Contrived ({self.letter}:{self.number})"

    def __lt__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented

        return self.sum() < other.sum()

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self.__dict__ == other.__dict__

    @staticmethod
    def _validate_letter(letter):
        if not isinstance(letter, str):
            raise TypeError("Argument must be a string")

        if len(letter) > 1 or letter not in string.ascii_letters:
            raise TypeError("Letter should be a single ascii character")

    @staticmethod
    def _validate_number(number):
        if number is None:
            raise TypeError("Number cannot be of type None")

        if not isinstance(number, int):
            raise TypeError
