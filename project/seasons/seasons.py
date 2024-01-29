import sys
import datetime
import inflect

p = inflect.engine()

def main():
    try:
        age = datetime.datetime.strptime(input('Day of Birth: ').strip(), '%Y-%m-%d').date()
        ageinminutes = ageinmin(age)
        print(ageinminutes)

    except:
        sys.exit('Invalid date')

def ageinmin(bday):
    delta = datetime.date.today() - bday
    minutesold = int(delta.total_seconds()//60)
    x = p.number_to_words(minutesold).replace(' and ',' ')
    x = x + ' minutes'
    return x.capitalize()

if __name__ == "__main__":
    main()
