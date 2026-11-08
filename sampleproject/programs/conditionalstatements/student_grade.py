
marks = int(input("enter the Student Marks :"))

if((marks <=100) and (marks>=70)):
    print("The Result is FCD!!!")
elif((marks<70) and (marks>=60)):
    print("The Result is First Class!!!")
elif((marks<60) and (marks>=50)):
    print("The Result is Second Class!!!")
elif((marks<50) and (marks>=35)):
    print("The Result is Pass Class!!!")
elif((marks<35) and (marks>=0)):
    print("The Result has failed")
else:
    print("Invalid Marks")
