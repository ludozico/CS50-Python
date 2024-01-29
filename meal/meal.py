def main():
    # Gets user time input and apply the function convert on it
    meal = convert(input('What time is it? '))

    # applies the conditions to determinte the output of the program
    if meal >= 7 and meal <=8:
        print('breakfast time')
    elif meal >= 12 and meal <=13:
        print('lunch time')
    elif meal >= 18 and meal <= 19:
        print('dinner time')
    else:
        return

# Convert the user input into the float number as asked
def convert(z):
    # converts the value for the hours
    time = z.split(':')
    if len(time[0]) < 2:
        x = z[0]
        x = float(x)
    else:
        x = z[:2]
        x = float(x)
    # converts the value for the minutes
    y = float(z[-2:])
    y = (y * (10/6))/100
    # adds up to the final value
    y = x + y
    # returns the value as the output of the convert function
    return round(y,2)

if __name__ == "__main__":
    main()
