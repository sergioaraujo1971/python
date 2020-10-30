import turtle
arcoires = ["red", "orange", "yellow", "green", "blue", "purple"]
ser=turtle.Turtle()
ser.width(5)
ser.penup()
ser.back(50)
ser.pendown()

for color in arcoires:
    ser.color(color)
    for lado in [1,2,3,4,5,6,7,8]:
        ser.pendown()
        ser.forward(40)
        ser.right(45)
    ser.penup()
    ser.left(60)

