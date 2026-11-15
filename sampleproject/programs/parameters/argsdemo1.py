# find sum of numbers [variabel length]
def sum_of_numbers(*args):
    sum=0
    for num in args:
        sum=sum +num
    print("sum of Numbers :",sum)
    print("---------")

sum_of_numbers(10,5)
sum_of_numbers(20)
sum_of_numbers(100,40,30)
sum_of_numbers(4,5,6,7,8,9)

