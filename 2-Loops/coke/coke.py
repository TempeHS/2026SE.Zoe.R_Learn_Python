#hholy shit i cant believe they added drugs to python

money = None
innedput = None

def cash():
    global money
    global innedput
    if money is None:
        money = 0
    innedput = int(input("how much money: "))
    if innedput == 5 or innedput == 10 or innedput == 25:
        money = innedput + money
    else:
        innedput = 0
        money = innedput + money

def moneycount():
    global money
    while money < 50:
        print (f"amount due: {50 - money}")
        cash()
    else:
        print("")
        print (f"change owed: {money - 50}")
        print ("enjoy ur coke lol")

cash()
moneycount()
