import re
import sys
" did not use the re | sys libs because it seemed easier like this " 
def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    count = 0
    ip = ip.split('.')
    if len(ip) == 4:
        for i in range(len(ip)):
            if ip[i].isdigit() and int(ip[i]) <= 255:
                print(ip[i])
                count += 1
            else:
                return False
        if count == 4:
            return True
        else:
            return False
    else:
        return False


if __name__ == "__main__":
    main()
