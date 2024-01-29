""" outdated task """
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
def main():
    while True:
        try:
            date = input('Date to be formated: ').strip()
            if date[0].isalpha():
                date = date.split(' ')
                if len(date) == 3 and date[1][-1] == ',':
                    mes = date[0]
                    dia = int(date[1].strip(','))
                    ano = date[2]
                else:
                    raise ValueError
                if date[0] in months and dia <= 31:
                    print(f"{ano}-{int(months.index(mes))+1:02d}-{dia:02d}")
                    break
                else:
                    raise ValueError
            elif date[0].isdigit():
                date = date.split('/')
                mes = int(date[0])
                dia = int(date[1])
                ano = date[2]
                if dia <= 31 and mes <= 12:
                    print(f"{ano}-{mes:02d}-{dia:02d}")
                    break
                else:
                    raise ValueError
            else:
                raise ValueError
        except ValueError:
            main()
main()




