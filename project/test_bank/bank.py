def main():
    # prompts the user for a greeting
    greeting = input("What's your greeting? ")
    money = value(greeting)
    print(f"${money}")

def value(greeting):
     if type(greeting) is str:
          greeting = greeting.strip().lower()
          if greeting.startswith('hello'):
               return 0
          elif greeting.startswith('h'):
               return 20
          else:
               return 100
     else:
          return 0

if __name__ == "__main__":
    main()

