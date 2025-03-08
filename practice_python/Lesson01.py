# Numeric Intiger
numeric_int : int = 20
numeric_float : float = 100.5
numeric_complex : complex = 3j

print(type(numeric_int),"Intiger = ", numeric_int)
print(type(numeric_float),"Float = ",numeric_float)
print(type(numeric_complex),"Complex Number = ",numeric_complex)




# Dictionary (Mapping Type)
dictionary : dict = {"Name":"Kashif Ali" , "age" : 20 , "Language" : "Hindko" , "Role":"Developer"}
# Add in Dictionary
dictionary["Institute"] = "GIAIC"
# Adding a New Key-Value Pair
dictionary["City"] = "Karachi"
# Removing a Key-Value Pair
del dictionary["City"]
# Using Dictionary Methods to Modify
dictionary.update({"Role":"Full Stack Developer"})
print(type(dictionary), "Dictionary" , dictionary )