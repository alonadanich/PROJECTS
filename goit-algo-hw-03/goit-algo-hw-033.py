"""
Завдання 3 (необов'язкове завдання). Ханойські башти
Напишіть програму, яка виконує переміщення 4 дисків з стрижня А на стрижень С, використовуючи стрижень В як допоміжний. Диски мають різний розмір і розміщені на початковому стрижні у порядку зменшення розміру зверху вниз.
Правила:
1. За один крок можна перемістити тільки один диск.
2. Диск можна класти тільки на більший диск або на порожній стрижень.
Вхідними даними програми має бути число n — кількість дисків на початковому стрижні. Вихідними даними — логування послідовності кроків для переміщення дисків зі стрижня А на стрижень С.
"""

def hanoi(n, source, target, auxiliary, state):
    if n == 1:
        move_disk(source, target, state)
    else:
        hanoi(n - 1, source, auxiliary, target, state)
        move_disk(source, target, state)
        hanoi(n - 1, auxiliary, target, source, state)

def move_disk(source, target, state):
    disk = state[source].pop()
    state[target].append(disk)
    print(f"\nПеремістити диск з {source} на {target}: {disk}")

def main():
    n = 4
    state = {
        "A": list(range(n, 0, -1)),
        "B": [],
        "C": []
    }
    print(f"Початковий стан: {state}")
    hanoi(n, "A", "C", "B", state)
    print(f"\nКінцевий стан: {state}")

if __name__ == "__main__":
    main()