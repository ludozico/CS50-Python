""" grocery task """
#initializing variables and their types
grocery = {}
# core loop
while True:
    try:
        item = input()
        grocery[item] = grocery.get(item, 0) + 1

    except EOFError:
            grocery = dict(sorted(grocery.items()))
            for item, count in grocery.items():
                 item = item.upper()
                 print(f"{count} {item}")
            break

