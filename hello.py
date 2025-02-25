def hello(to="world"):
    print("erm what the sigma", to)

# zoe was here
name = input ("What's your name? ")

# removes whitespace from string and capitalises name
name = name.strip().title()

# split user's name into first name and last name
first, last, what = name.split(" ")

print (f"hello, {first}")
hello(first)
