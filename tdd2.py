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
        return False
    else:
        listB = []
        for i in range(lenth-1):
            listB.append(round((listA[i+1]-listA[i])/t,2))
        return listB

def derivee2(listA,t):
    lenth = len(listA)
    if (lenth <=2):
        return False
    else:
        listB = derivee(listA,t)
        listC = []
        for i in range(lenth-2):
            listC.append(round((listB[i+1]-listB[i])/t,2))
        return listC


def derivee_func(func, g, p):
    if g==1 :
        dd = 0
    else :
        val = str(g)
        dd = len(val[val.find('.') + 1:])
    return round(func(p),dd)
