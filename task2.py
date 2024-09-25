import turtle

def koch_snowflake(t, order, size):
    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        size /= 3.0
        koch_curve(t, order - 1, size)
        t.left(60)
        koch_curve(t, order - 1, size)
        t.right(120)
        koch_curve(t, order - 1, size)
        t.left(60)
        koch_curve(t, order - 1, size)

def main():
    order = int(input("Введіть рівень рекурсії (0-5): "))
    if order < 0 or order > 5:
        print("Будь ласка, введіть коректний рівень (0-5).")
        return

    turtle.speed(0)
    turtle.penup()
    turtle.goto(-150, 90)
    turtle.pendown()
    turtle.hideturtle()

    koch_snowflake(turtle, order, 300)
    turtle.done()

if __name__ == "__main__":
    main()