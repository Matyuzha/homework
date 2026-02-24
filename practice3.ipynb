import math
import numpy as np
import matplotlib.pyplot as plt

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

# 1. Подготовка данных для графика основной функции
x_vals = np.linspace(0, 2, 400)
y_func = 10 * np.cos(x_vals) - 0.1 * x_vals**2

# 2. Подготовка данных для метода итераций (x и phi(x))
y_phi = np.arccos(0.01 * x_vals**2)

plt.figure(figsize=(12, 6))

# Левый график: Сама функция f(x) = 0
plt.subplot(1, 2, 1)
plt.plot(x_vals, y_func, label=r'$f(x) = 10\cos(x) - 0.1x^2$', color='blue')
plt.axhline(0, color='black', linewidth=1) # Линия y=0
plt.plot(x, 0, 'ro', label=f'Корень ≈ {x:.3f}') # Точка корня
plt.title('Поиск корня f(x) = 0')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True, linestyle='--')
plt.legend()

# Правый график: Точка пересечения y=x и y=phi(x)
plt.subplot(1, 2, 2)
plt.plot(x_vals, x_vals, label='y = x', color='gray', linestyle='--')
plt.plot(x_vals, y_phi, label=r'$y = \phi(x) = \arccos(0.01x^2)$', color='green')
plt.plot(x, x, 'ro', label='Точка итерации')
plt.title('Метод простой итерации')
plt.xlabel('x')
plt.grid(True, linestyle='--')
plt.legend()

plt.tight_layout()
plt.show()
