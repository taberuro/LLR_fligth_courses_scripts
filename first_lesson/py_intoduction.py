#Пример "Hello, World!" на Python:
print("Hello, World!")

#блок 2 пример 1
x = 5
if x > 0:
    print("x является положительным числом")

#блок 2 пример 2
x = -5
if x > 0:
    print("x является положительным числом")
else:
    print("x является отрицательным числом или нулем")

# блок 2 пример 3
x = 0
if x > 0:
    print("x является положительным числом")
elif x == 0:
    print("x равен нулю")
else:
    print("x является отрицательным числом")

# блок 3 пример 1
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)


# блок 3 пример 2

i = 1
while i <= 5:
    print(i)
    i += 1

# блок 4 пример 1

def sum(a, b):
    result = a + b
    return result

# блок 5 
# задание 1
def arithmetic(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        return num1 / num2
    else:
        return "Неизвестная операция"

print(arithmetic(2, 3, '+')) #5
print(arithmetic(4, 2, '-')) #2
print(arithmetic(5, 6, '*')) #30
print(arithmetic(8, 2, '/')) #4.0
print(arithmetic(7, 3, '%')) #'Неизвестная операция'


# задание 2
def is_year_leap(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False

print (is_year_leap(2000)) #True
print(is_year_leap(1900))#False

# задание 3
import math

def square(side):
    perimeter = 4 * side
    area = side ** 2
    diagonal = math.sqrt(2 * side ** 2)
    return (perimeter, area, diagonal)

print(square(5)) #(20, 25, 7.0710678118654755)
print(square(10)) #(40, 100, 14.142135623730951)
print(square(3)) #(12, 9, 4.242640687119285)

# задание 4
def season(month):
    if month in (1, 2, 12):
        return "Зима"
    elif month in (3, 4, 5):
        return "Весна"
    elif month in (6, 7, 8):
        return "Лето"
    elif month in (9, 10, 11):
        return "Осень"
    else:
        return "Неправильный номер месяца"

print (season(1)) # 'Зима'
print (season(4)) #'Весна'
print(season(8)) #'Лето'
print(season(11)) #'Осень'
print(season(13)) #'Неправильный номер месяца'

# задание 5
def bank(a, years):
    for i in range(years):
        a *= 1.1
    return a

print( bank(10000, 5) ) # 16105.100000000006
print(bank(5000, 3)) # 6655.000000000001
print(bank(20000, 10)) #67275.25311627773


# задание 6
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

print(is_prime(2)) # True
print(is_prime(7)) # True
print(is_prime(9)) # False
print(is_prime(1000)) # False

