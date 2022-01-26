#TDD2

def miroir(str,index):
    if(index < 0):
        return -1;
    str1 = str[0:index+1]
    str2 = str1[::-1]
    return(str1 + str2)



