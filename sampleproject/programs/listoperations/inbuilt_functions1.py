# Add Elements in to a List
flowers=[]
flowers.append("Lotus")
flowers.append("Sunflower")
flowers.append("Tulip")
# read Elements
print(flowers)
print("------------------")
# insert eleemnts existing list
fruits=["Mango","Apple","Banana"]
# insert
fruits.insert(1,"Grapes")
print(fruits)
print("------------------")
# count : It provide count of Elements
x=[10,20,30,10,20,10,20]
print(x.count(20))
print("------------------")
# len : to find number of Elements
x=[10,20,30,10,20,10,20]
print(len(x))
print("------------------")
# max , min, sum
x=[10,20,30,40]
print(max(x))
print(min(x))
print(sum(x))
print("------------------")
# Extends : combine Elements from both the list
a=[10,20,30]
b=[40,50,60,70]
a.extend(b)
print(a)
print("------------------")
# Remove : It removes Elements
cities=["Boston","Mysore","California","Sanjose","New york","Bangalore"]
cities.remove("California")       
print(cities) 
print("------------------")
# Pop : It removes and provides same element
cities=["Boston","Mysore","California","Sanjose","New york","Bangalore"]
print(cities.pop(3))
print(cities)