# I tried to make a calculator that would take the whole input in one go and return an answer, instead of taking one number or 
# operator at a time.


def calculate():
    #First I wanted to take the input as a string and store it in a list
    calculation = str(input('Enter your calculation: '))
    #The calclulationNumbers command utilises replace so that I can separate by whole numbers, instead of single digits.
    calculationNumbers = calculation.replace("+", " ").replace("/", " ").replace("*", " ").replace("-", " ")
    splitCalculation = calculationNumbers.split(" ")
    listOfNumbers = []
    #This loop adds each number from the input into a list of numbers
    for number in splitCalculation:
        listOfNumbers.append(int(number))
    listOfOperators = []
    #This loop adds each operator into a list of operators
    for parts in calculation:
        if parts == "+" or parts == "-" or parts == "/" or parts == "*":
            listOfOperators.append(parts)
    index = 0
    #This loop takes each number and uses the operator inbetween them to calculate an answer. The downside of this code is that the
    #calclulator can only do one calculation at a time, so 2+2 is fine but 2+2+2 wouldn't work.
    for index in range(len(listOfNumbers) - 1):
        for parts in listOfNumbers:
            if listOfOperators[index] == "+":
                answer = parts + listOfNumbers[index + 1]
                break
            if listOfOperators[index] == "-":
                answer = parts - listOfNumbers[index + 1]
                break
            if listOfOperators[index] == "/":
                answer = parts / listOfNumbers[index + 1]
                break
            if listOfOperators[index] == "*":
                answer = parts * listOfNumbers[index + 1]
                break
    print(calculation + " = " + str(answer))

calculate()

#I didn't add an On/Off function, as I was simply trying to solve a way to take a single input and use it to return a calculation.

