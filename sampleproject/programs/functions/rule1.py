def add(x,y):
    return (x + y)

def sub(a, b):
    result= (a - b)
    return result

def multiply(x, y):
    result=(x * y)
    print("Multiplication Result :",result)

# first Appraoch
v1=add(10,5)
v2=sub(35,25)
multiply(v1, v2)

# Second Approach
multiply(add(4,5), sub(10,5))
