MATHS = None

#asks for input
def no():
    global MATHS
    MATHS = input("enter your STINKY maths problem here: ")

def yes():
    #splits x y and z
    x, y, z = MATHS.split(" ")

    #convert x and z to integers
    x = int(x)
    z = int(z)

    #rounds the answer lol
    a_answer = round(x + z, 2)
    s_answer = round(x - z, 2)
    m_answer = round(x * z, 2)
    d_answer = round(x / z, 2)

    #checks if y is the correct symbol
    if y == "+":
        print(a_answer)
    elif y == "-":
        print(s_answer)
    elif y == "/":
        print(d_answer)
    elif y == "*":
        print(m_answer)
    else:
        print("womp womp, try again STUPID")
        no()
        yes()

no()
yes()
