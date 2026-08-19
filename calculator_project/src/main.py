print('Добро пожаловать в калькулятор!')
print('Доступные операции: +, -, /, *')
num1 = int(input('Введите первое число.'))
operation = input('+,-,/,*')
num2 = int(input('Введите второе число.'))
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '/':
    result = num1 / num2
elif operation == '*':
    result = num1 * num2
print(result)