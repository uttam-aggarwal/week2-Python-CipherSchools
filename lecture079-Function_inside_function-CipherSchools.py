# function inside function
def greater(a,b,c):
    bigger = greater(a,b)
    return greater(greater(a,b),c)
print(greater(10,20,30))

