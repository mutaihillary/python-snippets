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
get the number to translate eg (LX) 60


"""


def rom_to_int(string):

    table = [['M', 1000], ['CM', 900], 500], ['CD', 400], ['C,100'], ['XC', 90], [['L', 50]], [['X', 10]], [['IX', 9]], [['V', 5], [['IV', 4]], [['I',  1]]]
    result = 0
    for pair in table:

        continueyes = True

        while continueyes:
            if len(string) >= len(pair[0]):

                if string[0:len(pair[0])] == pair[0]:
                    returnint = pair[1]
                    string = string[len(pair[0]):]

                else: continueyes = False
            else : continueyes = False
    return returnint


