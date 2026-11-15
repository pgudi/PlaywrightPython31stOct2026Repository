# Empty Dictionary
products={}
# Add Elements
products["prodname"]="Lenovo Desktop"
products["price"]=45000,
products["quantity"]=200
products["prodid"]=101
# Read Each key value
print(products["prodname"])
print(products["price"])
# Read each value using get Method
print(products.get("prodname"))
print(products.get("price"))