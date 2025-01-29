"""
Завдання 2. Обчислення визначеного інтеграла
Ваше друге завдання полягає в обчисленні значення інтеграла функції методом Монте-Карло.
Можете обрати функцію на власний розсуд.
Виконаємо побудову графіка.

import matplotlib.pyplot as plt
import numpy as np
# Визначення функції та межі інтегрування
def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа

# Створення діапазону значень для x
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()

1. Обчисліть значення інтеграла функції за допомогою методу Монте-Карло, інакше кажучи, знайдіть площу під цим графіком (сіра зона).
2. Перевірте правильність розрахунків, щоб підтвердити точність методу Монте-Карло, шляхом порівняння отриманого результату та аналітичних розрахунків або результату виконання функції quad. Зробіть висновки.
 Для перевірки обчислення визначеного інтеграла в Python ви можете використовувати бібліотеку SciPy, зокрема її функцію quad з підмодуля integrate. Спочатку необхідно визначити функцію, яку ви хочете інтегрувати, а потім використати quad для обчислення інтеграла на заданому інтервалі.
Приклад застосування функції quad
import scipy.integrate as spi

# Визначте функцію, яку потрібно інтегрувати, наприклад, f(x) = x^2
def f(x):
    return x**2

# Визначте межі інтегрування, наприклад, від 0 до 1
a = 0  # нижня межа
b = 2  # верхня межа

# Обчислення інтеграла
result, error = spi.quad(f, a, b)
print("Інтеграл: ", result, error)
У цьому прикладі, функція quad повертає два значення: результат інтегрування та оцінку абсолютної помилки.
Виведення:
Інтеграл:  2.666666666666667 2.960594732333751e-14
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

def f(x):
    return 3 * x + 2

a = 1
b = 6

N = 100000
x_random = np.random.uniform(a, b, N)
y_random = np.random.uniform(0, f(b), N)

under_line = y_random <= f(x_random)
monte_carlo_area = (b - a) * f(b) * np.sum(under_line) / N

analytical_result, error = spi.quad(f, a, b)

print(f"Результат методом Монте-Карло: {monte_carlo_area:.6f}")
print(f"Результат функції quad: {analytical_result:.6f}")
print(f"Абсолютна помилка методу Монте-Карло: {abs(analytical_result - monte_carlo_area):.6f}")

x = np.linspace(a, b, 500)
y = f(x)

plt.figure(figsize=(8, 6))
plt.plot(x, y, label="f(x) = 3x + 2", color="blue")
plt.fill_between(x, 0, y, alpha=0.3, label="Область під прямою", color="gray")
plt.scatter(x_random, y_random, s=1, alpha=0.2, label="Випадкові точки")
plt.xlim([a - 0.5, b + 0.5])
plt.ylim([0, f(b) + 0.5])
plt.axhline(0, color="black", linewidth=0.5)
plt.axvline(a, color="gray", linestyle="--")
plt.axvline(b, color="gray", linestyle="--")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Інтегрування методом Монте-Карло та функцією quad")
plt.legend()
plt.grid()
plt.show()