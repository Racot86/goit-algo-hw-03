import turtle


def koch_curve(t, length, depth):
    if depth == 0:
        t.forward(length)
    else:
        koch_curve(t, length / 3, depth - 1)
        t.left(60)
        koch_curve(t, length / 3, depth - 1)
        t.right(120)
        koch_curve(t, length / 3, depth - 1)
        t.left(60)
        koch_curve(t, length / 3, depth - 1)


def koch_snowflake(t, length, depth):
    for _ in range(3):
        koch_curve(t, length, depth)
        t.right(120)


def main():
    screen = turtle.Screen()
    screen.setup(width=600, height=600)
    t = turtle.Turtle()
    t.speed(0)

    recursion_level = int(input("Enter recursion level: "))

    t.penup()
    t.goto(-150, 90)
    t.pendown()
    koch_snowflake(t, 300, recursion_level)

    t.hideturtle()
    screen.mainloop()


if __name__ == "__main__":
    main()
