#this one was pretty easy lol
#it's kinda just a modified version of problem 1
vowels = input("your message here: ")

#goes through all the characters in the input
for char in vowels:
    #finds the vowels
    match char:
        case "a" | "e" | "i" | "o" | "u" | "A" | "E" | "I" | "O" | "U":
            #replaces them with nothing
            char = ""
    #prints out all the characters individually without any spaces between them
    print (char, end = "")
print("")
