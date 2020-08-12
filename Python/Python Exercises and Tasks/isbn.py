# ISBN's (International Standard Book Numbers) are identifiers for books. 

# The ISBN is a thirteen-digit code.

# The last digit is a check number calculated as follows:
# •	The first 12 digits are taken
# •	Starting at index 1, if the index is odd - add it, and if the index is even – multiply the digit by three then add it.
# •	From the sum find the remainder after dividing by 10.
# •	10 minus the remainder give us the check digit
# •	In other words the following algebra would give us the check digit:
# ( 10 – (( x1 + 3x2 + x3 + 3x4 + x5 + 3x6 + x7 + 3x8 + x9 + 3x10 + x11 + 3x12 ) % 10))



import random

isbn = []

for i in range(12):
    i = random.choice(range(10))
    isbn.append(i)

print(isbn)

def lastnum():
    index = 0
    last = 0
    while index < 12:
        if index % 2 != 0:
            last = isbn[index] + last
        else:
            last = int(isbn[index]) * 3 + last
        index += 1
    remainder = last % 10
    answer = 10 - remainder
    isbn.append(answer)
    print(isbn)

lastnum()