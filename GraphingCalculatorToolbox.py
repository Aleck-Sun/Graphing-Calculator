def makeGraph(eqn):
    getABCvalues(eqn)

def getABCvalues(eqn):
    #Globalizing values we will use for graphing calculations and inputs
    global a, b, c

    #If not quadratic
    if "^" not in eqn:
        a = 0
        
        #Coefficient of x is 0
        if "x" not in eqn:
            b = 0
            c = float(eqn[2:])

        else:
            slope = eqn.find("x")
            
            #No coefficient in front of b (b = 1)    
            if slope == 2:
                b = 1

            #Negative sign infront of b
            elif eqn[slope-1] == "-":
                b = -1

            else:
                b = float(eqn[2:slope])
            
            cDetermine = eqn[slope+1:]

            #if c = 0
            if cDetermine == "":
                c = 0
                
            else:
                c = float(cDetermine)

    #Finding a, b, c for quadratic equation 
    else:
        expo = eqn.find("^")
        
        #If no coefficient in front of x^2 (1)
        if expo-1 == 2:
            a = 1

        #Negative sign in front of x^2, coeffiecient of -1
        elif eqn[expo-2] == "-":
            a = -1

        else:
            a = float(eqn[2:expo-1])

        newEqn = eqn[expo+2:]

        #0 coefficient for x
        if "x" not in newEqn:
            b = 0
            cDetermine = newEqn

            #If c = 0
            if cDetermine == "":
                c = 0
            else:
                c = float(cDetermine)
                print(c)

        else:
            slope = newEqn.find("x")

            #No coefficient infront of x (1)
            if slope == 1:
                b = 1

            #Negative sign infront of b
            elif newEqn[slope-1] == "-":
                b = -1

            else:
                b = float(newEqn[:slope])

            cDetermine = newEqn[slope+1:]

            #If c = 0
            if cDetermine == "":
                c = 0
            
            else:
                c = float(cDetermine)

def drawAxes(xMin, xMax, xIncrement, yMin, yMax, yIncrement, width, height, s):
    #Globalizing values we will use for graphing calculations
    global spaceX, spaceY, originX, originY
    
    #Coordinate Label Arrays
    numberX = []
    numberY = []

    #Appending axes tick mark labels (min to max, jumping by increments)
    for i in range(xMin, xMax + xIncrement, xIncrement):
        numberX.append(i)

    for i in range(yMin, yMax + yIncrement, yIncrement):
        numberY.append(i)
    
    #Spacing on canvas(Amount of space between 1 unit)
    spaceX = width/(xMax-xMin)
    spaceY = height/(yMax-yMin)

    #Coordinates Array
    X = []
    Y = []
    x = 0
    y = height

    #Appending canvas coordinates of axes
    for i in range(len(numberX)):
        X.append(x)
        x += spaceX*xIncrement

    for i in range(len(numberY)):
        Y.append(y)
        y -= spaceY*yIncrement

    #Origin on canvas(Distance between 0 and minimum)
    originX =(0-xMin) * spaceX
    originY = (0-yMin) * spaceY

    #Drawing axes:
    #x-axis ticks
    for i in range(len(numberX)):
        s.create_line(X[i], originY + 5, X[i], originY - 5, width = 2)
        #0 only needs to be printed once
        if numberX[i] != 0:
            s.create_text(X[i], originY + 15, text = str(numberX[i]), font = "arial 10")

    #y-axis ticks
    for i in range(len(numberY)):
        s.create_line(originX + 5, Y[i], originX - 5, Y[i], width = 2)
        if numberY[i] != 0:
            s.create_text(originX - 15, Y[i], text = str(numberY[i]), font = "arial 10")

    #Origin Point (Only has to be labelled once)
    s.create_text(originX - 10, originY + 10, text = "0", font = "arial 10")

    #x and y axes
    s.create_line(0, originY, width, originY, width = 2)
    s.create_line(originX, 0, originX, height, width = 2)

def TableOfValues(xMin, xMax, numPoints, s):
    global X, Y
    #Variables
    pointIncrement = (xMax - xMin)/numPoints
    xValue = []
    yValue = []
    X = []
    Y = []
    x = xMin

    #Appending actual x and y values
    for i in range (numPoints):
        y = a*x**2 + b*x + c
        xValue.append(x)
        yValue.append(y)
        x += pointIncrement

    #Calculating points on canvas with actual values
    for i in range(numPoints):
        X.append(originX + xValue[i] * spaceX)
        Y.append(originY - yValue[i] * spaceY)

##def plotPoints(X, Y):   
    #Plotting points and connecting them with a line
    for i in range(numPoints):
        if i != numPoints-1:
            s.create_oval(X[i]-1, Y[i]-1, X[i]+1, Y[i]+1)
            s.create_line(X[i], Y[i], X[i+1], Y[i+1])
            s.create_oval(X[i+1]-1, Y[i+1]-1, X[i+1]+1, Y[i+1]+1)
