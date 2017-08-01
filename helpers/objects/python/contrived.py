from functools import total_ordering


@total_ordering
class Contrived:

    def __init__(self, letter, number):
        self.letter = letter
        self.number = number

    def __str__(self):
        return f"Contrived ({self.letter}:{self.number})"

    def __lt__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        if self.letter == other.letter:
            return self.number < other.number

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self.__dict__ == other.__dict__
