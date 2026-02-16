import math

print("ПРАКТИЧЕСКАЯ РАБОТА №3")
print("Метод простой итерации")
print("Уравнение: 10*cos(x) - 0.1*x^2 = 0")
print("-" * 50)

# Функция для итерационного процесса x = φ(x)
def phi(x):
    return math.acos(0.01 * x * x)

# Начальное приближение
x = 1.5
eps = 0.001
max_iter = 20

print(f"Начальное x0 = {x}")
print(f"Точность: {eps}")
print()

for i in range(max_iter):
    x_old = x
    x = phi(x_old)
    
    print(f"Итерация {i+1}: x{i} = {x_old:.6f} -> x{i+1} = {x:.6f}, |x{i+1}-x{i}| = {abs(x - x_old):.6f}")
    
    if abs(x - x_old) < eps:
        print(f"\nТочность достигнута на {i+1}-й итерации!")
        print(f"Корень уравнения: x = {x:.6f}")
        print(f"Округленно: x = {x:.3f}")
        break
else:
    print(f"\nДостигнуто максимальное число итераций ({max_iter})")
