import random

x = -1
while True:
    x = input('Level: ')
    if x.isdigit():
        x = int(x)
        if x > 0:
            break

y = random.randint(1,x)

while True:
    reply = input('Guess: ')
    if reply.isdigit():
        reply = int(reply)
        if reply < y:
            print('Too small!')
        elif reply > y:
            print('Too large!')
        else:
            print('Just right!')
            break
