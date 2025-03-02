vowels = input("your message here: ")

for char in vowels:
    match char:
        case "a" | "e" | "i" | "o" | "u" | "A" | "E" | "I" | "O" | "U":
            char = ""
    print (char, end = "")
print("")
