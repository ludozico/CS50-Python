""" adieu task """
import sys
nameslist = []
reply = "Adieu, adieu, to "
towhom = str()
lastname = str()
while True:
    try:
        name = input('')
        nameslist.append(name)
    except EOFError:
        if len(nameslist) == 1:
            print(reply+nameslist[0])
            break
        elif len(nameslist) == 2:
            print(f"{reply}{nameslist[0]} and {nameslist[1]}")
            break
        else:
            for name in nameslist[:-1]:
                towhom += name + ', '
                lastname = f"and {nameslist[-1]}"

        print(reply+towhom+lastname)
        sys.exit(0)
