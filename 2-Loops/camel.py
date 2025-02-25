camel = input("camelCase text here: ")

for char in camel:
    if char.isupper():
        char = char.lower()
        char = "_" + char
    print (char, end = "")
print("")
