def main():
    # gets prompt from the user
    twitter = input('Type your message here: ')
    print(shorten(twitter))

def shorten(word):
    twttr = ''
    # for loop
    for char in word:
        if char in ['A','a','E','e','I','i','O','o','U','u']:
            pass
        else:
            twttr = twttr + char
    return twttr

if __name__ == "__main__":
    main()
