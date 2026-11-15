
def getFactorial(num):
    if(num==1):
        return 1
    return num * getFactorial(num-1)

print(getFactorial(4))
print(getFactorial(5))
print(getFactorial(6))

''' How it works
 print(getFactorial(5))
5 * getFactorial(4)
5 * 4 * getFactorial(3)
5 * 4 * 3 * getFactorial(2)
5 * 4 * 3 * 2 * getFactorial(1)
5 * 4 * 3 * 2 * 1
'''