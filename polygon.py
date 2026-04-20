import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("Turtle Python")

turtle_instance= turtle.Turtle()
turtle_instance_2= turtle.Turtle()
turtle_instance_3= turtle.Turtle()

while True:
    try:
        num_sides= int(input("Enter the number of edges for the polygon you want to draw: "))
        angle = 360.0/num_sides
        side_lenght = 100
        for i in range(num_sides):
            turtle_instance.right(angle)
            turtle_instance.forward(side_lenght)
    except:
        print("Please enter a number!")
    else:
        break




turtle.done()