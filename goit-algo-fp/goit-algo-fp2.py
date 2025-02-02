"""
Завдання 2. Рекурсія. Створення фрактала “дерево Піфагора” за допомогою рекурсії
Необхідно написати програму на Python, яка використовує рекурсію для створення фрактала “дерево Піфагора”. Програма має візуалізувати фрактал “дерево Піфагора”, і користувач повинен мати можливість вказати рівень рекурсії.
"""
import turtle

def draw_branch(t, branch_length, level):
    if level == 0:
        return
    t.forward(branch_length)

    new_lenght = branch_length * 0.7

    t.left(45)
    draw_branch(t, new_lenght, level - 1)
    t.right(45)

    t.right(45)
    draw_branch(t, new_lenght, level - 1)
    t.left(45)

    t.backward(branch_length)

def main():
    recursion_level = int(input("Введіть рівень рекурсії: "))

    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.title("Дерево Піфагора")

    t = turtle.Turtle()
    t.speed(0)
    t.left(90)
    t.up()
    t.goto(0, -250)
    t.down()
    t.pensize(3)
    t.color("brown")

    draw_branch(t, 100, recursion_level)

    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()