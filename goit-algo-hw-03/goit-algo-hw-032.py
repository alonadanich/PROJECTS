"""
Завдання 2
Напишіть програму на Python, яка використовує рекурсію для створення фракталу «сніжинка Коха» за умови, що користувач повинен мати можливість вказати рівень рекурсії.
"""
import turtle

def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.right(angle)

def draw_koch_snowflake(order, size=300):
    window = turtle.Screen()
    window.bgcolor("lightblue")
    
    t = turtle.Turtle()
    t.speed(0)
    t.color("blue")
    t.pensize(4)
    t.penup()
    t.goto(-size / 2, -size / (2 * (3**0.5)))
    t.pendown()

    for _ in range(3):
        koch_curve(t, order, size)
        t.right(-120)

    window.mainloop()

if __name__ == "__main__":
    order = int(input("ВВедіть рівень рекурсії: "))
    draw_koch_snowflake(order)
