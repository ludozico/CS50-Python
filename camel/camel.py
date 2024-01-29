# Gets the prompt
camel = input('Insert your variable name here:')
# initialize variable snake
snake = ''
# iterate over the camel variable name
for letter in camel:
    # transcribe uppercase letters while changing the style to snake
    if letter.isupper():
        snake = snake + '_' + letter.lower()
    # transcribe lowercase letters into the new variable
    else:
        snake = snake + letter

# fixes small bug
if snake[0] == '_':
    snake = snake[1:]
else:
 None

# prints final version
print(snake)



