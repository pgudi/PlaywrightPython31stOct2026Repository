# split function
s1="Mango,Banana,Ornage,Apple"
result=s1.split(",")
for item in result:
    print(item)

print("--------------------")
# lstrip  It trims from left hand side
# rstrip  It trims from right hand side
# strip  It trims from both side
s2="   Welcome   "
print("Before lstrip, Number of Characters :",len(s2))
print("After lstrip, Number of Characters :",len(s2.lstrip()))
print(s2.lstrip())
print("Before rstrip, Number of Characters :",len(s2))
print("After rstrip, Number of Characters :",len(s2.rstrip()))
print(s2.rstrip())
print("Before strip, Number of Characters :",len(s2))
print("After strip, Number of Characters :",len(s2.strip()))
print(s2.strip())
print("--------------------")
# Capitalize : only first character of first word changes to upper case
# Title: Each word first character changes to uppercase
s4="python program practice"
print(s4.capitalize())
print(s4.title())
