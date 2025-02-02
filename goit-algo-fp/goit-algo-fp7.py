"""
Завдання 7. Використання методу Монте-Карло
Необхідно написати програму на Python, яка імітує велику кількість кидків кубиків, обчислює суми чисел, які випадають на кубиках, і визначає ймовірність кожної можливої суми.
Створіть симуляцію, де два кубики кидаються велику кількість разів. Для кожного кидка визначте суму чисел, які випали на обох кубиках. Підрахуйте, скільки разів кожна можлива сума (від 2 до 12) з’являється у процесі симуляції. Використовуючи ці дані, обчисліть імовірність кожної суми.
На основі проведених імітацій створіть таблицю або графік, який відображає ймовірності кожної суми, виявлені за допомогою методу Монте-Карло.
Таблиця ймовірностей сум при киданні двох кубиків виглядає наступним чином.

Порівняйте отримані за допомогою методу Монте-Карло результати з аналітичними розрахунками, наведеними в таблиці вище.
"""
import numpy as np
import matplotlib.pyplot as plt

num_rolls = 1000000

dice1 = np.random.randint(1, 7, num_rolls)
dice2 = np.random.randint(1, 7, num_rolls)
sums = dice1 + dice2

unique, counts = np.unique(sums, return_counts=True)
probabilities = counts / num_rolls

analytical_probs = {
    2: 1/36, 3: 2/36, 4: 3/36, 5: 4/36, 6: 5/36, 7: 6/36, 8: 5/36, 9: 4/36, 10: 3/36, 11: 2/36, 12: 1/36
}

print("Сума | Імовірність Монте-Карло | Імовірність теоретична")
print("-" * 50)
for value, prob in zip(unique, probabilities):
    print(f"{value:>2} | {prob:.4%} ({prob:.4f}) | {analytical_probs[value]:.4%} ({analytical_probs[value]:.4f})")

plt.bar(unique, probabilities, alpha=0.7, label="Монте-Карло", color="blue")
plt.scatter(analytical_probs.keys(), analytical_probs.values(), color="red", label="Аналітичні", zorder=2)
plt.xlabel("Сума значень двох кубиків")
plt.ylabel("Імоірність")
plt.xticks(range(2, 13))
plt.legend()
plt.title("Порівняння імовірностей: Монте-Карло та Аналітичні")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()