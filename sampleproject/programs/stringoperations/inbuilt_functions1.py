# Inbuilt Functions in String
# format
# Default Formating
s="{} {} {}".format("Python", "Programming","Language")
print(s)

# Based on Position
s="{2} {1} {0}".format("Python", "Programming","Language")
print(s)

# Based on Keyword
s="{q} {p} {r}".format(p="Python", q="Programming", r="Language")
print(s)

# Display 3rd Table

for i in range(1,11):
    v1=f"{3 } * {i} = {3 * i}"
    print(v1)