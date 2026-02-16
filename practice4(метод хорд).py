import math

print("ПРАКТИЧЕСКАЯ РАБОТА №4")
print("Метод хорд")
print("Уравнение: 10*cos(x) - 0.1*x^2 = 0")
print("-" * 50)

# Исходная функция
def f(x):
    return 10 * math.cos(x) - 0.1 * x * x

# Границы отрезка [a, b]
a = 1.5
b = 1.55
eps = 0.001
max_iter = 20

print(f"Отрезок: [{a}, {b}]")
print(f"f({a}) = {f(a):.6f}")
print(f"f({b}) = {f(b):.6f}")
print(f"Точность: {eps}")
print()

# Выбираем неподвижную точку c
if abs(f(a)) < abs(f(b)):
    c = a
    x = b
    print(f"Неподвижная точка c = {c}, начальное x0 = {x}")
else:
    c = b
    x = a
    print(f"Неподвижная точка c = {c}, начальное x0 = {x}")
print()

for i in range(max_iter):
    x_old = x
    # Формула метода хорд
    x = (c * f(x_old) - x_old * f(c)) / (f(x_old) - f(c))
    
    print(f"Итерация {i+1}: x{i+1} = {x:.6f}, |x{i+1}-x{i}| = {abs(x - x_old):.6f}")
    
    if abs(x - x_old) < eps:
        print(f"\nТочность достигнута на {i+1}-й итерации!")
        print(f"Корень уравнения: x = {x:.6f}")
        print(f"Округленно: x = {x:.3f}")
        break
else:
    print(f"\nДостигнуто максимальное число итераций ({max_iter})")
