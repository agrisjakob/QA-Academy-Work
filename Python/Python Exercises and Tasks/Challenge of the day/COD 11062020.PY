#Write a function which returns the boolean True if the input is only divisible by one and itself.
#
#The function should return the boolean False if not.
#two(3) → True
#two(8) → False


def func(input):
    for i in range(1, input):
        if i != input and i !=1 and input % i == 0:
            return False
        else:
            return True

print(func(3))