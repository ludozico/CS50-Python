#""" fuel exercise """
# loop to get right input
def main():
    try:
        fraction = input("What's the fraction of your tank? ").strip()
        fraction = fraction.split('/')
        X = int(fraction[0])
        Y = int(fraction[1])

        if X <= Y:
            if X/Y > 0.01 and X/Y < 0.99:
                print(str((round((X/Y)*100)))+'%')
            elif X/Y <= 0.01:
                print('E')
            elif X/Y >= 0.99:
                print('F')
        elif Y == 0:
            raise ZeroDivisionError
        else:
            raise ValueError
    except (ValueError):
        print("Use a valid fraction with 2 integer!")
        main()
    except ZeroDivisionError:
        print("Can't divide by zero")
        main()

main()

