"""
Create a function that:
	1. Halves even numbers
	2. Doubles odd numbers
	3. Returns the sum of all
	pseudo code
define initial number and get numbers
check if it is even or odd
if odd number halves other doubles odd number
get the sum of all numbers
print

"""
numbers = [2,3]

def best_way(number):
    even = 0
    odd = 0
    for i in number:
        if i % 2 == 0:
             even = even + (int(i) / 2)
        elif i % 2 != 0:
             odd = odd + (int(i) * 2)
             result = even + odd
    return result

print best_way(numbers)