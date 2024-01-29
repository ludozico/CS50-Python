def main():
    plate = input("Plate: ")
    print(is_valid(plate))

def is_valid(s):
    if not (2 <= len(s) <= 6):  # Check plate length is between 2 and 6
        return False

    if not s[0:2].isalpha():  # First two characters must be letters
        return False

    num_started = False
    for char in s:
        if not char.isalnum():  # No special characters allowed
            return False
        if num_started and char.isalpha():  # No letters allowed after numbers have started
            return False
        if char.isdigit():
            if not num_started:
                # Check if the first digit is '0'
                if char == '0':
                    return False
                num_started = True  # Numbers have started

    return True  # All checks passed

if __name__ == "__main__":
    main()
