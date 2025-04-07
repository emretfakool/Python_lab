import math

# Завдання 1
print("Завдання 1: Площа трьох прямокутників")
for i in range(1, 4):
    a = float(input(f"Введіть сторону a прямокутника {i}: "))
    b = float(input(f"Введіть сторону b прямокутника {i}: "))
    area = a * b
    print(f"Площа прямокутника {i}: {area}")

# Завдання 2
print("\nЗавдання 2: Гіпотенузи двох прямокутних трикутників")

def hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)

a1 = float(input("Катет 1 трикутника 1: "))
b1 = float(input("Катет 2 трикутника 1: "))
a2 = float(input("Катет 1 трикутника 2: "))
b2 = float(input("Катет 2 трикутника 2: "))

h1 = hypotenuse(a1, b1)
h2 = hypotenuse(a2, b2)

print(f"Гіпотенуза трикутника 1: {h1}")
print(f"Гіпотенуза трикутника 2: {h2}")

if h1 > h2:
    print("Гіпотенуза трикутника 1 більша.")
elif h1 < h2:
    print("Гіпотенуза трикутника 2 більша.")
else:
    print("Гіпотенузи рівні.")

# Завдання 3
print("\nЗавдання 3: Перевірка, які точки всередині кола")

def is_inside_circle(x, y, a, b, R):
    return (x - a)**2 + (y - b)**2 < R**2

a = float(input("Центр кола - координата a: "))
b = float(input("Центр кола - координата b: "))
R = float(input("Радіус кола: "))

p1 = float(input("P: координата x: "))
p2 = float(input("P: координата y: "))
f1 = float(input("F: координата x: "))
f2 = float(input("F: координата y: "))
l1 = float(input("L: координата x: "))
l2 = float(input("L: координата y: "))

count = 0
if is_inside_circle(p1, p2, a, b, R): count += 1
if is_inside_circle(f1, f2, a, b, R): count += 1
if is_inside_circle(l1, l2, a, b, R): count += 1

print(f"Кількість точок всередині кола: {count}")

# Завдання 4
print("\nЗавдання 4: Площа чотирикутника, де кут між X і Y – прямий")

X = float(input("Сторона X: "))
Y = float(input("Сторона Y: "))
Z = float(input("Сторона Z: "))
T = float(input("Сторона T: "))

# Перша частина — прямокутний трикутник
S1 = 0.5 * X * Y
diag = math.sqrt(X**2 + Y**2)

# Друга частина — трикутник через формулу Герона
s = (diag + Z + T) / 2
S2 = math.sqrt(s * (s - diag) * (s - Z) * (s - T))

total_area = S1 + S2
print(f"Загальна площа чотирикутника: {total_area}")

# Завдання 5
print("\nЗавдання 5: Пошук чисел, які діляться на всі задані")

n = int(input("Введіть n: "))
divisors = list(map(int, input("Введіть числа (через пробіл), на які має ділитися результат: ").split()))

result = []
for i in range(1, n + 1):
    if all(i % d == 0 for d in divisors):
        result.append(i)

print("Числа, що задовольняють умову:")
print(result)
