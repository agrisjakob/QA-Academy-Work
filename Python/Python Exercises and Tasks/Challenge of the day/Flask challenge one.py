#CHALLENGE OF THE DAY

#Write a FUNCTION which takes an integer input, a, and returns the sum a+aa+aaa+aaaa.

#So if 2 was the input, the function should return 2+22+222+2222 which is 2468.

#three(9) → 11106
#three(5) → 6170



def three(i):
    String = str(i)
    first = int(String)
    second = int(String * 2)
    third = int(String * 3)
    fourth = int(String * 4)
    added = first + second + third + fourth
    return added

print(three(9))    




