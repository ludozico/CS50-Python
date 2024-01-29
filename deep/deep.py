# Gets prompt from the user
answer = input('What its the answer to the Great Question of Life, the Universe and Everything? ')
# Prepares the prompt
answer = answer.lower().strip()
# matchs the answer
match answer:
    case '42' | 'forty-two' | 'forty two':
        print('Yes')
    case _:
        print('No')
