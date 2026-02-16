import math

print("ПРАКТИЧЕСКАЯ РАБОТА №4")
print("Метод касательных (Ньютона)")
print("Уравнение: 10*cos(x) - 0.1*x^2 = 0")
print("-" * 50)

# Исходная функция
def f(x):
    return 10 * math.cos(x) - 0.1 * x * x

# Производная функции
def f_derivative(x):
    return -10 * math.sin(x) - 0.2 * x

# Начальное приближение (берем правый конец отрезка)
x = 1.55
eps = 0.001
max_iter = 20

print(f"Начальное x0 = {x}")
print(f"f(x0) = {f(x):.6f}")
print(f"f'(x0) = {f_derivative(x):.6f}")
print(f"Точность: {eps}")
print()

for i in range(max_iter):
    x_old = x
    # Формула метода касательных
    x = x_old - f(x_old) / f_derivative(x_old)
    
    print(f"Итерация {i+1}: x{i+1} = {x:.6f}, |x{i+1}-x{i}| = {abs(x - x_old):.6f}")
    
    if abs(x - x_old) < eps:
        print(f"\nТочность достигнута на {i+1}-й итерации!")
        print(f"Корень уравнения: x = {x:.6f}")
        print(f"Округленно: x = {x:.3f}")
        break
else:
    print(f"\nДостигнуто максимальное число итераций ({max_iter})")
