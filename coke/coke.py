#Initialize the variable total
total = 0
# Gets input from the user
print('Amount Due: ' + str(50 - total))
# loop
while total < 50:
        coin = input('Insert coin here: ')
        if coin in ['5','10','25']:
                total += int(coin)
                if total >= 50:
                        print('Change Owed:', abs(50 - total))
                        break
                else:
                      print('Amount Due: ' + str(50 - total))

        else:
                        print('Amount Due: ' + str(50 - total))
                        coin = input('Insert coin here: ')



