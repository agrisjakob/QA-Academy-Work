# Question: Write a program that accepts a comma separated sequence of words as input and prints 
# the words in a comma-separated sequence after sorting them alphabetically. 
# Suppose the following input is supplied to the program: without,hello,bag,world Then, 
# the output should be: bag,hello,without,world



def sorter(sequence):
    lst = sequence.split(',')
    lst.sort()
    newSequence = ""
    for i in lst:
        newSequence = newSequence + i + ","
    return newSequence


print(sorter("without,hello,bag,world"))