
def sum_digits(a):
    # Step 1 : initialize a total for the sum value
    total = 0

    # Step 2 : Loop through the list (a)
    for i in a:

        # Step 3 : Loop through individual numbers as string characters using str()
        for x in str(i):

            # Step 4 : As the Loop goes round, add each character as an integer to the total value
            total = int(x) + total

        # Step 5 : return the total value
        return total

    # Step 6 : print out
print sum_digits([10,20,30])

