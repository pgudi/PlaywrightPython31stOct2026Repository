# split function
s1="Mango,Banana,Ornage,Apple"
result=s1.split(",")
print(result)
# By default it takes delimiter as space
s2="Bangalore and Mysore Cities"
result2=s2.split()
print(result2)
print("---------------")
#find -> It seaches the string provides position [left to right]
s3="It is a book, It is on the table, is it?"
print(s3.find("is"))
print(s3.find("It"))
print(s3.find("is",7))  # Second occcurance of is
print(s3.find("is",19))  # Third occurance of is
print(s3.find("Welcome"))
print("---------------")
#rfind -> It seaches the string provides position [right to left]
s3="It is a book, It is on the table, is It?"
print(s3.rfind("is"))
print(s3.rfind("It"))
print("---------------")
#index -> It seaches the string provides position [left to right]
s3="It is a book, It is on the table, is it?"
print(s3.index("is"))
print(s3.index("It"))
print(s3.index("is",7))  # Second occcurance of is
print(s3.index("is",19))  # Third occurance of is
#print(s3.index("Welcome"))  # It provides Error
print("---------------")
#rindex-> It seaches the string provides position [right to left]
s3="It is a book, It is on the table, is It?"
print(s3.rindex("is"))
print(s3.rindex("It"))
print("---------------")