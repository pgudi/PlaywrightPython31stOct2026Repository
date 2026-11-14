# Without Return value
def findFactorial(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    print("The Factorial of ",num," is ",fact)

findFactorial(4)
findFactorial(5)
findFactorial(6)
print("---------------------")
# using return concept
def getFactorial(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    return fact

print("the Outpur :",getFactorial(4))
print("The FActorial Result :",getFactorial(5))
print(getFactorial(6))