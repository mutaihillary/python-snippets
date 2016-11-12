def calculate_tax(income_input="dictionary", data={"Alex": 500, "James": 20500, "Kinuthia": 70000}):
    for item in income_input():
        if (income_input >= 0) and (income_input <= 1000):
            tax = (0 * income_input)

        elif (income_input > 1000) and (income_input <= 10000):
            tax = (0.1 * (income_input - 1000))

        elif (income_input > 10000) and (income_input <= 20200):
            tax = ((0.1 * (10000 - 1000)) + (0.15 * (income_input - 10000)))

        elif (income_input > 20200) and (income_input <= 30750):
            tax = ((0.1 * (10000 - 1000)) + (0.15 * (20200 - 10000)) +
                   (0.2 * (income_input - 20200)))

        elif (income_input > 30750) and (income_input <= 50000):
            tax = ((0.1 * (10000 - 1000)) + (0.15 * (20200 - 10000)) +
                   (0.2 * (30750 - 20200)) + (0.25 * (income_input - 30750)))

        elif (income_input > 50000):
            tax = ((0.1 * (10000 - 1000)) + (0.15 * (20200 - 10000)) +
                   (0.2 * (30750 - 20200)) + (0.25 * (50000 - 30750)) +
                   (0.3 * (income_input - 50000)))
        else:
            pass
            keys = set(data)
            return income_input, keys