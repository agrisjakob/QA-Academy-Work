#Write a function that returns the factorial of a number

def factorial(number):
    answer = 1
    for i in range(1, int(number)+1):
        answer = answer * i
    return answer


