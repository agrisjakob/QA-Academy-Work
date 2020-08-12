	# INSTRUCTIONS

	# In case it is not clear, the Question appears first, then examples, then any hints and finally the function that you need to complete appears underneath:

	# <QUESTION>

	# <EXAMPLES>

	# <HINT>

	# You are NOT allowed access to the internet for this assessment, instead you should use the DOCUMENTATION that comes bundled with your Python installation.  You should already be comfortable accessing this documentation, but to summarise:

	# Access Python from you CLI

	# Type help() or for example help(str)



	# <QUESTION 1>    
	
	# Given a string, return a string where for every char in the original string, there are three chars.
    
    # <EXAMPLES>

	# one("The") → "TTThhheee"
	# one("AAbb") → "AAAAAAbbbbbb"
	# one("Hi-There") → "HHHiii---TTThhheeerrreee"

	# <HINT>
	# How does a for loop iterate through a string?

def one(input):
    answer = ""
    for i in input:
        answer = answer + i*3
    return answer

	# <QUESTION 2>

    #  Write a function which returns the boolean True if the input is only divisible by one and itself.
    
    # The function should return the boolean False if not.

	# <EXAMPLES>

    # two(3) → True
    # two(8) → False

	# <HINT>
	# What operator will give you the remainder?
	# Use your CLI to access the Python documentation and get help manipulating strings - help(range).

def two(input):
    if input == 2:
        return True
    if input == 0 or input == 1:
        return False
    for i in range(2, input):
        if input == i:
            continue
        if input % i == 0:
            return False
        else:
            return True


	# <QUESTION 3>

    # Write a function which takes an integer input, a, and returns the sum a+aa+aaa+aaaa.

	# So if 2 was the input, the function should return 2+22+222+2222 which is 2468.

	# <EXAMPLES>

	# three(9) → 11106
	# three(5) → 6170

	# <HINT>
	# What happens if you multiply a string by a number?

def three(a):
    String = str(a)
    first = int(String)
    second = int(String * 2)
    third = int(String * 3)
    fourth = int(String * 4)
    added = first + second + third + fourth
    return added

	# <QUESTION 4>

    # Given two Strings of equal length, 'merge' them into one String.

    # Do this by 'zipping' the Strings together.

    # Start with the first char of the first String.
    # Then add the first char from the second String.
    # Then add the second char from the first String.
    # And so on.

    # Maintain case.

    # You will not encounter whitespace.
    
    # <EXAMPLES>

	# four("String","Fridge") → "SFtrriidngge"
	# four("Dog","Cat") → "DCoagt"
	# four("True","Tree") → "TTrrueee" 
	# four("return","letter") → "rleettutrenr"

	# <HINT>
	# Use your CLI to access the Python documentation and get help manipulating strings - help(list.insert).
	# How would you seperate a string into characters?

def four(input1, input2):
    lst1 = []
    lst2 = []
    answer=[]
    for i in input1:
        lst1.append(i)
    for n in input2:
        lst2.append(n)
    for x in range(len(input1)):
        answer.append(lst1[x])
        answer.append(lst2[x])
    finalAnswer = "".join(answer)    
    return finalAnswer

	# <QUESTION 5>

	# Write a function to randomly generate a list with 5 even numbers between 100 and 200 inclusive.
    
    # <EXAMPLES>
    
    # five() → [100,102,122,198,200]
    # five() → [108,104,106,188,200]
    # five() → [154,102,132,178,164]
    
	# <HINT>
	# There is a module which can be used to generate random numbers, this module is called random.
	# The random module contains a function called randint.

import random
def five():
    answer = []
    lst= list(range(100,201,2))
    for i in range(5):
        number = random.choice(lst)
        answer.append(number)
    return answer

	# <QUESTION 6>

	# Given a string, return the boolean True if it ends in "py", and False if not. 
	
	# Ignore Case.

	# For Example:

	# six("ilovepy") → True
	# six("welovepy") → True
	# six("welovepyforreal") → False
	# six("pyiscool") → False

	# <HINT>
	# There are no hints for this question.
    
def six(input):
    input = input.lower()
    if input[-2] == "p" and input [-1] == "y":
        return True
    else:
        return False

	# <QUESTION 7>

    # Given three ints, a b c, one of them is small, one is medium and one is large. 
	
	# Return the boolean True if the three values are evenly spaced, so the
	# difference between small and medium is the same as the difference between
	# medium and large. 
	
	# Do not assume the ints will come to you in a reasonable order.
    
    # <EXAMPLES>

	# seven(2, 4, 6) → True
	# seven(4, 6, 2) → True
	# seven(4, 6, 3) → False
	# seven(4, 60, 9) → False

	# <HINT>
	# There is a function for lists called sort.
	# Use the cli to access the documentation help(list.sort)

def seven(a, b, c):
    lst = [a,b,c]
    sortedlst = sorted(lst)
    if sortedlst[1] - sortedlst[0] == sortedlst[2] - sortedlst[1]:
        return True
    else:
        return False


	# <QUESTION 8>

    # Given a string and an integer, n, return a string that removes n letters from the 'middle' of the string.
	
	# The string length will be at least n, and be odd when the length of the input is odd, so there will always be a 'middle'.

    # <EXAMPLES>

	# eight("Hello", 3) → "Ho"
	# eight("Chocolate", 3) → "Choate"
	# eight("Chocolate", 1) → "Choclate"

	# <HINT>
    # Use the cli to access the documentation help(str.replace)

def eight(input,  a):
    input = list(input)
    for i in range(a):
        middle = int(len(input)/ 2)
        input.pop(middle)
    answer = "".join(input)
    return answer

	# <QUESTION 9>

    # Given two string inputs, if one can be made from the other return the boolean True, if not return the boolean False.

	# <EXAMPLES>

    # nine("god", "dog") → True
    # nine("tree", "tiredest") → True
    # nine("cat", "dog") → False
    # nine("tripping", "gin") → True

	# <HINT> 
	# There are no hints for this question.

def nine(string1, string2):
    lst1 = list(string1)
    lst2 = list(string2)
    lst2match = []
    lst1match = []
    for letter in lst1:
        for character in lst2:
            if letter == character:
                lst2match.append(character)
                lst2.remove(character)
                break
    lst2 = list(string2)
    for letter in lst2:
        for character in lst1:
            if letter == character:
                lst1match.append(character)
                lst1.remove(character)
                break
    print(lst1match, lst2match)
    lst1 = list(string1)
    lst2 = list(string2)
    if lst1 == lst2match or lst2 == lst1match:
        return True
    else:
        return False

	# <QUESTION 10>

    # Write a function which takes 2 integers greater than 0, X,Y as input and generates a 2-dimensional array. 
	
	# The element value in the i-th row and j-th column of the array should be i*j.

	# <EXAMPLES>

	# ten(3,2) → [[0,0,0],[0,1,2]]
	# ten(2,1) → [[0,0]]
	# ten(3,4) → [[0,0,0],[0,1,2],[0,2,4],[0,3,6]]

	# <HINT>
	# Think about nesting for loops.

def ten(X,Y):
    lst= []
    for i in range(0, Y):
        nestlst = []
        for n in range(0, X):
            nestlst.append(i*n)
        lst.append(nestlst)
    return lst