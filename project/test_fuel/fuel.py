#""" fuel exercise """
# loop to get right input
def main():
    y = convert(input("What's the fraction of your tank? ").strip())
    print(gauge(y))

def convert(fraction):
    fraction = fraction.split('/')
    X = int(fraction[0])
    Y = int(fraction[1])
    if X <= Y:
        Z = (X/Y)*100
        Z = round(Z)
        return(Z)
    elif Y == 0:
        raise ZeroDivisionError
    else:
        raise ValueError

def gauge(percentage):
    if percentage >= 99:
        return 'F'
    elif percentage <= 1:
        return 'E'
    else:
        x = str(percentage)+'%'
        return x



if __name__ == "__main__":
    main()

