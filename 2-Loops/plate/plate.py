#this one lowkey made me want to set something on fire 
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        #if the function is_valid returns true, then it prints that the plate is valid
        print("Valid")
    else:
        #and vice versa if it returns false
        print("Invalid")


#this entire function is basically just a really long series of if statements for if the 
#plate is valid or not
def is_valid(s):
    #counts all the letters in the variable to make sure its between 2 and 6
    if len(s) >= 2 and len(s) <= 6:
        #if the entire string is letters, return true
        if s.isalpha():
            return True
        #the first part of this checks to see if the string is letters AND numbers
        #(if the string is all numbers it's invalid by default)
        #the second part of this checks if the first two characters are letters
        elif s.isalnum() and s[0:2].isalpha():
            for char in s:
                #if the characters after the first two are numbers, check their position
                if char.isdigit():
                    position = s.index(char)
                    #checks to see if every character after the number is also a number
                    #and checks to make sure the first number isnt 0
                    #if both of these are the case, return true
                    if s[position:].isdigit() and int(char) != 0:
                        return True
                    #otherwise return false, etc, etc
                    else:
                        return False

main()