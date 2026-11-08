s1="good morning"
print(s1.islower())
print("-----------")
s2="MORNING"
print(s2.isupper())
print("-----------")
s3="welcome"
print(s3.isalpha())
print("-----------")
s4="welcome123"
print(s3.isalnum())
print("-----------")
s5="1234"
print(s5.isdigit())
print(s5.isnumeric())
print(s5.isdecimal())
print("-----------")
# count : it provides count of character or words
s6="It is a book, It is on table, It is history book"
print(s6.count("is"))
print(s6.count("It"))
print("-----------")
# Length : It provides Number of chars 
s6="Welcome"
print(len(s6))
print("-----------")
# Join Function joins multiple Elements
s7=" "
print(s7.join(["it","is","on","the","table"]))
print("-----------")
# not in operator
s8="Lotus is a flower"
print("fruit" not in s8)
print("fruit" in s8)
print("-----------")
# is operator : it verifies the eference
ss1="Welcome"
ss2="Welcome"
print(ss1 is ss2)  # It verifies the reference
print(ss1 == ss2)  # Verifies teh content
a="program"
b=a
print(a is b)  # It verifies the reference
print(a == b)  # Verifies teh content
print("-----------")
c="Writing"
d="writing"
print(c is d)  # It verifies the reference
print(c.lower() == d)  # Verifies teh content
print(c is not d) # It verifies the reference