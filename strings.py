## Numbers, strings and tuples are immutable datatypes


string1="Star"
string2="Wars"

# String concatination
print("# String concatination")
print("tring1 + String2", string1+string2)

# String repitation
print("# String repitation")
print("String1",(string1+string2)*5)

# String slicing

print("# String slicing")
print(string1[0:2])

print(string1[3])
print(string1[-1])

#type specific method

print(string1.count('s',0,3))

print(string1.isalnum())