def main():
    menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }
    price = 0
    while True:
        try:
            item = input('Item: ').title()
            if item in menu:
                price += menu[item]
                print(f'${price:.2f}')
        except EOFError:
            #first time using this string formatation style, seems better now (no cheating <3)
            print(f'\nTotal price: ${price:.2f}')
            break



main()
