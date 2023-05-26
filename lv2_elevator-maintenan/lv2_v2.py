l = ["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"]


def solution(l):
    inputList= l
    
    #print("Input list = ", inputList)
    list1 = [] 

    for x in inputList:
        list1.append(x.split("."))
    #print("List 1 = ", list1)
    list2 = [] 

    for y in list1:
        y = list(map(int, y))
        list2.append(y)
    #print("List2 = ", list2)
    list3 = sorted(list2) 
    #print("List 3 (sorted List = ", list3)
    outputList = [] 

    for a in list3:
        a = '.'.join(str(z) for z in a)
        outputList.append(a)
    #print("Output List = ",  outputList)

    return outputList

print(solution(l))