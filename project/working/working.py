import re
import sys

def main():
    print(convert(input("Hours: ").strip()))

def convert(s):
    #Regex
    if matches := re.search(r'^(\d{1,2}):?(\d{2})? (AM|PM) to (\d{1,2}):?(\d{2})? (AM|PM)$',s):
        # naming like a pro
        hours_1, minutes_1, cond1, hours_2, minutes_2, cond2 = matches.groups()

        # if no min, then 00
        if minutes_1 == None:
            minutes_1 = '00'
        if minutes_2 == None:
            minutes_2 = '00'

        # if bugged time, Error
        if int(minutes_1) >= 60 or int(minutes_1) < 0:
            raise ValueError
        if int(minutes_2) >= 60 or int(minutes_2) < 0:
            raise ValueError
        if int(hours_1) > 12 or int(hours_1) < 1:
            raise ValueError
        if int(hours_2) > 12 or int(hours_2) < 1:
            raise ValueError

        # converting PM to normal hours for time 1
        if cond1 == 'PM':
            if hours_1 != '12':
                hours_1 = str(int(hours_1) + 12)
            else:
                pass
        # converting AM to normal hours for time 1
        if cond1 == 'AM':
            if hours_1 == '12':
                hours_1 = '0'
            else:
                pass

        #converting PM to normal hours for time 2
        if cond2 == 'PM':
            if hours_2 != '12':
                hours_2 = str(int(hours_2) + 12)
            else:
                pass
        # converting AM to normal hours for time 2
        if cond2 == 'AM':
            if hours_2 == '12':
                hours_2 = '0'
            else:
                pass

        # formating hours 1 # > ##
        if int(hours_1) < 10:
            hours_1 = '0'+ hours_1
        else:
            pass

        # formating hours 2 # > ##
        if int(hours_2) < 10:
            hours_2 = '0'+ hours_2
        else:
            pass

        # finalizing
        hours = f'{hours_1}:{minutes_1} to {hours_2}:{minutes_2}'
        return hours
    else:
        raise ValueError


if __name__ == "__main__":
    main()
