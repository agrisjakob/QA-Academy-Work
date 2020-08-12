# Challenge
# •	Create an application which asks the user for an input for a maths mark, a chemistry mark and a physics mark. 
# •	Add the marks together, then work out the overall percentage. And print it out to the screen.
# •	If the percentage is below 40%, print “You failed”
# •	If the percentage is 40% or higher, print “D”
# •	If the percentage is 50% or higher, print “C”
# •	If the percentage is 60% or higher, print “B”
# •	If the percentage is 70% or higher, print “A”


maths = int(input("Enter your Maths grade: "))
chem = int(input("Enter your Chemistry grade: "))
phys = int(input("Enter your Physics grade: " ))



def averageGrade():
        average = (maths + chem + phys) / 3
        return average

def actualGrade():
        if averageGrade() > 70:
            print("You scored a grade of A.")
        elif averageGrade() > 60:         
            print("You scored a grade of B.")
        elif averageGrade() > 50:
            print("You scored a grade of C.")
        elif averageGrade() > 40:
            print("You scored a grade of D")        
        else:
            print("You failed.")
    

print("Your average grade is: ", averageGrade())
averageGrade()
actualGrade()      