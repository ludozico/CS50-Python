import random

def main():
    lvl = get_level()
    score = 0
    # Loop for each question
    for _ in range(10):
        # just learned i can define 2 variables in a tupple like this
        x, y  = generate_integer(lvl)
        # defining the correct answer
        z = x + y
        # inializing my counter to zero for each question
        counter = 0
        # loop to assure the user only has 3 shots
        while counter < 3:
            w = input(f"{x} + {y} = ")
            # wrong answer branch
            if not w.isdigit() or int(w) != z:
                counter += 1
                print('EEE')
                if counter == 3:
                    print(f"{x} + {y} = {z}")
                    break
            # correct answer branch
            else:
                score += 1
                break

    # Final score:
    print(f"Score: {score}")


def get_level():
    while True:
        lvl = input('Level: ')
        if lvl.isdigit():
            lvl = int(lvl)
            if lvl > 0 and lvl <= 3:
                return lvl


def generate_integer(level):
    if level == 1:
        x = random.randint(0,9)
        y = random.randint(0,9)
    elif level == 2:
        x = random.randint(10,99)
        y = random.randint(10,99)
    else:
        x = random.randint(100,999)
        y = random.randint(100,999)
    return x,y








if __name__ == "__main__":
    main()
