import turtle

def koch_curve(t, length, level):
    if level == 0:
        t.forward(length)
    else:
        length /= 3.0
        koch_curve(t, length, level-1)
        t.left(60)
        koch_curve(t, length, level-1)
        t.right(120)
        koch_curve(t, length, level-1)
        t.left(60)
        koch_curve(t, length, level-1)

def koch_snowflake(t, length, level):
    for _ in range(3):
        koch_curve(t, length, level)
        t.right(120)

def main():
    screen = turtle.Screen()
    screen.bgcolor("white")
    
    t = turtle.Turtle()
    
    while True:
        level = int(input("Введіть рівень рекурсії (від 0 до 6, бо задовбетесь чекати якщо вище): "))
        if 0 <= level <= 6:
            break
        else:
            print("Будь ласка, введіть значення між 0 і 6.")
    
    length = 300
    
    t.penup()
    t.goto(-length // 2, length // 2)
    t.pendown()
    
    koch_snowflake(t, length, level)
    
    turtle.done()

if __name__ == "__main__":
    main()
