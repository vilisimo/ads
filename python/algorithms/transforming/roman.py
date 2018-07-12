# Dicts are guaranteed to retain insertion order in 3.7
NUMERALS = {
    "M": 1000,
    "CM": 900,
    "D": 500,
    "CD": 400,
    "C": 100,
    "XC": 90,
    "L": 50,
    "XL": 40,
    "X": 10,
    "IX": 9,
    "V": 5,
    "IV": 4,
    "I": 1,
}


def generate(number):
    if not isinstance(number, int):
        raise ValueError('Input should be an integer')

    if not 0 < number < 4000:
        raise ValueError('Integer should fall within the following interval: [1, 3999]')

    result = []
    for key, value in NUMERALS.items():
        while value <= number:
            number -= value
            result.append(key)

    return ''.join(result)
