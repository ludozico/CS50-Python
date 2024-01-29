""" ALMOST THERE <3 LETS GOOO! LAST EXERCISE FORM WEEK 7 hehe """

import validators

def main():
    print(validate(input("What's your email addres? ")))

def validate(email):
    try:
        response = validators.email(email)
        if response == True:
            return 'Valid'
        else:
            return 'Invalid'
    except TypeError:
        return 'Invalid'

if __name__ == "__main__":
    main()
