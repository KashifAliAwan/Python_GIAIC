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



# Boolean
boolean_type : bool = False
boolean_type : bool = True
print(type(boolean_type), "Boolean = " , boolean_type)


# Set 
set_variable : set = {2,3,4,5,5,6,7,8,9,10,1}
print(type(set_variable), "Set = " , set_variable)

# Froozenset
frozenset_variable : frozenset = frozenset({"kashif ali","ali","kashif ali",5,2,55,55,8,6,15,10,1})
print(type(frozenset_variable),"Frozen Set = ",frozenset_variable)



# String

text_double: str  = "Hello, Python!" # Strings with Double Quotes (")
text_single: str  = 'Hello, Python!' # Strings with Single Quotes (')
text_multi: str   = '''Hello, 
                                      Python!''' # Multi-Line Strings with Triple Quotes (''' or """)
text_multi_1: str = """Hello, 
                                      Python!""" # Multi-Line Strings with Triple Quotes (''' or """)

print(type(text_double), " text_double   = ", text_double)    # <class 'str'>
print(type(text_single), " text_single   = ", text_single)    # <class 'str'>
print(type(text_multi), " text_multi    = ", text_multi)      # <class 'str'>
print(type(text_multi_1), " text_multi_1  = ", text_multi_1)  # <class 'str'>
