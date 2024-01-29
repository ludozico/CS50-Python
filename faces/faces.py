# Function to convert emoticons to emojis
def convert(x):
    x = x.replace(':)','🙂')
    x = x.replace(':(','🙁')
    return x

text = input('Insert your text here: ')
print(convert(text))

