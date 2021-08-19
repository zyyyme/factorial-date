import math
from datetime import datetime


def factorial_date():
    date_string = input('Enter date: ')

    try:
        datetime.strptime(date_string, '%d/%m/%Y')
    except:
        print('Date does not match pattern DD/MM/YYYY. Try again.')
        return

    total = 0

    for element in date_string:
        if element.isnumeric():
            total += int(element)

    print('Factorial of all digits in date: ', total, '! = ', math.factorial(total), sep='')


if __name__ == "__main__":
    factorial_date()