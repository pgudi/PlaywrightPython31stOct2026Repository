'''
Assignment 2: Programmatically add numbers in between 1 to 100, which are divisible by 8 and find the sum of All Elements.
Step 1: Make sure we can print numbers from 1 to 100
Step 2: Among 1 to 100 print numbers which are divisible by 8
Step 3:  Create an empty list
Step 4: Programmatically add numbers in between 1 to 100, which are divisible by 8
Step 5: find the sum of All Elements in a list
'''
divisibleEight=[]
for i in range(1,101):
    if(i % 8 ==0):
        divisibleEight.append(i)

print(divisibleEight)
# Sum of All Elements
sum=0
for i in range(0, len(divisibleEight)):
    sum=sum+divisibleEight[i]

print(sum)