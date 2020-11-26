from GraphingCalculatorToolbox import *
from tkinter import *
width = 1000
height = 1000

myInterface = Tk()
s = Canvas(myInterface, width = width, height = height, background = "white")
s.pack()

#Stars
stars = "*" * 70

#Introduction to program:
print(stars)
print("""
Welcome to the linear and quadratic graphing calculator!

Here is how it works:
This graphing calculator allows the user(you) to input a linear or
quadratic equation for y. It also creates axes based on inputted values.
It then graphs the equation onto the axes inputted.

EQUATION:
Enter an equation in the form y=ax^2+bx+c

Rules when entering equation:
1) When typing the equation, don't type spaces between characters
2) The symbol for the exponent 2 is "^2"
3) Include "y=" at the beginning
4) You may type coefficients of 0 and 1 if you would like
   HOWEVER:
   For coefficients of 0, you can type nothing
   ex. a = 0, type bx+c // a and b = 0, type y=c

   For coefficients of 1, you can type no coefficient
   ex. a = 1, type x^2+bx+c // b = 1, type ax^2+x+c

AXES:
The program draws axes that stretch from one end of the canvas to the other.

To draw the axes the user(you) will input:
- minimum and maximum points for the x and y axes
- the jump/increment of each x and y coordinate on the axes (Must be positive)

NOTE:
If the coordinate 0 never appears between minimum and maximum, the user(you) will
not see the axes and it's labels since the axes will be off the canvas
""")
print(stars)
print()

#Inputs:
Quit = False
while Quit == False:
    #Inputs
    #Axes
    #xAxes
    xMin = int(input("Enter minimum x value:  "))
    xMax = int(input("Enter maximum x value:  "))
    xIncrement = int(input("Enter x increment/jump value:  "))
    print()

    #yAxes
    yMin = int(input("Enter minimum y value:  "))
    yMax = int(input("Enter maximum y value:  "))
    yIncrement = int(input("Enter y increment/jump value:  "))
    print()

    #Number of x points
    numPoints = int(input("Enter number of points to graph:  "))

    drawAxes(xMin, xMax, xIncrement, yMin, yMax, yIncrement, width, height, s)
    
    #Creating equations
    eqn = input("Enter equation:  ")
    makeGraph(eqn)
    TableOfValues(xMin, xMax, numPoints, s)

    s.update()
    
    #If user would like to draw more graphs
    more = input("Would you like to create more graphs?(y/n):  ")
    if more == "y":
        s.delete("all")
        s.update()
    else:
        Quit = True
