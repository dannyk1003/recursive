number1 = int(input('input 1:'))
number2 = int(input('input 2:'))

def GCD(number1, number2):
    if number1 < number2:
        number1, number2 = number2, number1
    else:
        number = number1 % number2
        if number != 0:
            return GCD(number2, number)
        else:
            return number2

answer = GCD(number1, number2)

print(f'{number1}, {number2} GCD = {answer}')