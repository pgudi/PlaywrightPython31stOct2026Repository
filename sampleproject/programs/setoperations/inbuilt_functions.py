# Declare an Empty Set
fruits={"Watermelon"}
# Add Elements in to a Set
fruits.add("Mango")
fruits.add("Grapes")
fruits.add("Orange")
fruits.add("Banana")
fruits.add("Mango")
print(fruits)
# Remove element
fruits.remove("Orange")
print(fruits)
print("----------------")
#pop
flowers={"Lotus",140,True,"Sunflower","Lilly"}
print(flowers)
v1=flowers.pop()
print(v1)
print(flowers)
v1=flowers.pop()
print(v1)
print(flowers)
print("----------------")
# Copy function : It copies the existing set
flowers={"Lotus",140,True,"Sunflower","Lilly"}
print(flowers)
flowersNew=flowers.copy()
print(flowersNew)
print("----------------")
# update
flowers={"Lotus",140,True,"Sunflower","Lilly"}
print(flowers)
flowers.update({"Mango","Apple","Banana"})
print(flowers)
print("----------------")
# Clear
flowers={"Lotus",140,True,"Sunflower","Lilly"}
print(flowers)
flowers.clear()
print(flowers)