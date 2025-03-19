#hholy shit i cant believe they added drugs to python

money = None
innedput = None

def cash():
    global money
    global innedput
    #sets money to 0 if the user hasn't inputted anything
    if money is None:
        money = 0
    #gets the user input
    innedput = int(input("how much money: "))
    #if input = 5, 10 or 25, add the input to the current money value
    if innedput == 5 or innedput == 10 or innedput == 25:
        money = innedput + money
    #if not, make the input 0
    else:
        innedput = 0
        money = innedput + money

def moneycount():
    global money
    #if the money is under 50, print the amount due
    while money < 50:
        print (f"amount due: {50 - money}")
        cash()
    #if not, print the change owed and give them COKE
    else:
        print("")
        print (f"change owed: {money - 50}")
        print ("enjoy ur coke lol")

cash()
moneycount()
