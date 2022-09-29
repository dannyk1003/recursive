number = int(input('n = '))

def fibonacci(number):
    if number <= 1:
        return number
    else:
        return fibonacci(number-1) + fibonacci(number-2)


print(f'{number} fibonacci = {fibonacci(number)}')