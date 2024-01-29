#Prompt the user for the expression
def main(math):
    math = math.strip().split()
    x = float(math[0])
    y = math[1]
    z = float(math[2])
    if y == '+':
        print(round((x + z),1))
    elif y == '-':
        print(round((x - z),1))
    elif y == '*':
        print(round((x * z),1))
    elif y == '/':
        y = x / z
        y = round(y,1)
        print(y)
    else:
        print("Can't accept")

main(input('Insert the expression here: '))

