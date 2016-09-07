# Scrabble Score

# Write a program that, given a word, computes the scrabble score for that word.
# Letter Values

# You'll need these:


# Letter                           Value
#      1 A, E, I, O, U, L, N, R, S, T       1
#      2 D, G                               2
#      3 B, C, M, P                         3
#      4 F, H, V, W, Y                      4
#      5 K                                  5
#      6 J, X                               8
#      7 Q, Z                               10

# Examples

#     "cabbage" should be scored as worth 14 points:

#         3 points for C
#         1 point for A, twice
#         3 points for B, twice
#         2 points for G
#         1 point for E

#     And to total:

#         3 + 2*1 + 2*3 + 2 + 1
#         = 3 + 2 + 6 + 3
#         = 5 + 9
#         = 14
def scrabble_score(word):

    score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, "l": 1,
             "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, "x": 8, "z": 10}
    if not word.isalpha():
        return 0
    return sum(score[let] for let in word.lower())



