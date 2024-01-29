import re
import sys

def main():

    print(count(input("Text: ")))

def count(s):
    try:
        counter = 0
        ums = re.findall(r'\bum\b',s,flags=re.IGNORECASE)
        for i in range(len(ums)):
            counter += 1
    except TypeError:
        return 0
    return counter

if __name__ == "__main__":
    main()
