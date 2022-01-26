#TDD2

def miroir(str,index):
    if(index < 0):
        return -1;
    str1 = str[0:index+1]
    str2 = str1[::-1]
    return(str1 + str2)


def derivee(listA,t):
    lenth = len(listA)
    if (lenth <=1):
        return -1
    else:
        listB = []
        for i in range(lenth-1):
            listB.append(round((listA[i+1]-listA[i])/t,2))
        return listB
