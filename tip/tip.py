def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    # take out the $ sign
    d = float(d.strip('$'))
    # make sure its ##.##
    d = round(d,2)
    return d


def percent_to_float(p):
    # take out the % sign
    p = float(p.strip('%'))
    # ensure that its 00.## as asked
    p = round(p/100,2)
    print(p)
    return p

main()
