answer = input ("answer: ")

match answer:
    case "42" | "fourty two" | "Fourty Two" | "Fourty two" | "fourty-two" | "Fourty-Two" | "Fourty-two":
        print("yes")
    case "fourty Two" | "fourty-Two":
        print("yes but also why would you write it like that")
    case _:
        print("no")
