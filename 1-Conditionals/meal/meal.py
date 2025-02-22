#I know the problem said to format this code a certain way
#but i wasnt really sure what i was supposed to do with the formatting that was given
#so i just used this code that i wrote before i solved that part
#(which does work)
#since i could really figure out what the given code does
#(especially the last part)
#if i figure it out later i'll come back to this code and edit it

time = input("what time is it? ")

hour, minute = time.split(":")
hour = int(hour)

if hour == 7 or hour == 8:
    print("breakfast time")
elif hour == 12 or hour == 13:
    print("lunch time")
elif hour == 18 or hour == 19:
    print ("dinner time")
