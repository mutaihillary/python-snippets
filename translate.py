# Given a roman numeral as input, write a function that converts the roman
# numeral to a number and outputs it.
#
# Ex:
# translateRomanNumeral("LX") # 60
#
# When a smaller numeral appears before a larger one, it becomes
# a subtractive operation. You can assume only one smaller numeral
# may appear in front of larger one.
#
# Ex:
# translateRomanNumeral("IV") # 4
#
# You should return `nil` on invalid input.
"""
pseudo code
define a function
get a list of Romans with their corresponding integer values.
get the number to translate eg (LX) 60

Assign value to their corresponding figures in integer
 Output the results
"""


def rom_to_int(hillary):
    result = 0
    hillary = hillary.upper()

    table = [['M', 1000], ['CM', 900], ['D', 500], ['CD', 400], ['C', 100], ['XC', 90], ['L', 50], ['XL', 40],
             ['X', 10], ['IX', 9], ['V', 5], ['IV', 4], ['I', 1]]

    for letter, value in table:
        while hillary.startswith(letter):
            result += value
            hillary = hillary[1:]
    return result

user = raw_input("Enter Roman Numeral: ")
print rom_to_int(user)
