# 4. Write a function to count of prime numbers in between 50 to 100?
def find_count_of_prime(start, end):
    count=0
    for i in range(start, end):
        flag=0
        for k in range(2,i):
            if(i % k==0):
                flag=flag+1
                break
        if(flag==0):
            count=count+1
    print("count of Prime Numbers :",count)

find_count_of_prime(50,101)
