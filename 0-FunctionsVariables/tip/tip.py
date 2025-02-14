#i love coding.

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? ")) # type: ignore
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    result = d.replace("$","")
    return float (result)


def percent_to_float(p):
    sigma = p.replace('%','')

    return float (sigma) / 100


main()