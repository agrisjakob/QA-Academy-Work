

def merge(string1, string2):
    lst1 = []
    lst2 = []
    answer=[]
    for i in string1:
        lst1.append(i)
    for n in string2:
        lst2.append(n)
    for x in range(len(string1)):
        answer.append(lst1[x])
        answer.append(lst2[x])
    return answer

print(merge("String", "Fridge"))