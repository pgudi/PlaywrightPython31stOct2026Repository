
def multiply_numbers(*args):
    result=1
    for num in args:
        result=result * num
    print("Multiplication Result :",result)
    print("------")

multiply_numbers(5)
multiply_numbers(4,5,6)
multiply_numbers(10,3,8,2)
multiply_numbers(2,3,4,5,6,7)