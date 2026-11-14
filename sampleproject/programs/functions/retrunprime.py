def isPrime(num):
    flag=True
    for i in range(2,num):
        if(num % i ==0):
            flag=False
            break
    if(flag==True):
        return True
    else:
        return False

# First Appraoch
v1=isPrime(29)
print("Is it a Prime Number :",v1)
# Second Appraoch
# Print Prime numbers in between 10 to 40
for i in range(10,41):
    if(isPrime(i)==True):
        print(i)
# Third Appraoch
# Print counto f Prime Numbers in between 50 100
count=0
for i in range(50,101):
    if(isPrime(i)==True):
        count=count+1
print("Count of Prime Numbers :",count)

# Sum of Prime Prime Numbers in between 1 to 50
sum=0
for i in range(50,101):
    if(isPrime(i)==True):
        sum=sum+i
print("Sum of Prime Numbers :",sum)