#Create a function that when given two strings of letters, determine whether the second can be made from 
#the first by removing one letter. The remaining letters must stay in the same order.


def near(word1,word2):
    index = 0
    near = False
    while index < len(word1):
    
        word1List = []
        word2List = []
    
        for i in word1:
            word1List.append(i)
        for l in word2:
            word2List.append(l)       
        print("word1 list is:" , word1List)

       
        del word1List[index]
        print("word1 list is: ", word1List)
        print("word2 list is: ", word2List)
        if word1List == word2List:
            near = True
            break
        else:
            near = False
        index += 1
        
    if near == True:
        print(True)
    else:
        print(False)


near("reset", "rest")        