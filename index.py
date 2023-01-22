#config
player = "\x1b[32mO\x1b[0m"
enemy = "\x1b[31mO\x1b[0m"
length = 7
height = 6


def buildField(gamefield):
    for column in gamefield:
        columnString = "|"
        for spot in column:
            columnString = columnString + spot + "|"
        print(columnString)


def turn(who):
    turnActive = True
    while turnActive == True:
        i = input("Where would you like to place your " + who + "? ")
        if (i.isnumeric()):
            if (int(i) <= length and int(i) >= 0):
                if (field[0][int(i) - 1] == "_"):
                    for j in range(height):
                        row = field[j]
                        if (row[int(i) - 1] != "_"):
                            field[j - 1][int(i) - 1] = who
                            turnActive = False
                            break
                        elif (j == height - 1):
                            row[int(i) - 1] = who 
                            turnActive = False
                else:
                    print("That column is full!")
            else:
                print("Enter a number 1 - " + str(length) + ".")
        else:
            print("Enter a valid number.")

def checkForWin(gamefield, who):

    #checkDraw
    draw = True
    for row in gamefield:
        if (row.__contains__("_")):
            draw = False
    if (draw == True):
        print("Draw!")
        return True

    # horizontal
    for row in gamefield:
        array = []
        for spot in row:
            if (spot != "_"):
                if (len(array) == 0):
                    array.append(spot)
                elif (spot == array[len(array) - 1]):
                    array.append(spot)
                else:
                    array = [spot]

                if (len(array) >= 4):
                    print(who + " won the game!")
                    return True
            else:
                array = []  

    #vertical
    for column in range(length):
        array = []
        for row in range(height):
            spot = field[height - 1 - row][column]
            if (spot != "_"):
                if (len(array) == 0):
                    array.append(spot)
                elif (spot == array[len(array) - 1]):
                    array.append(spot)
                else:
                    array = [spot]

                if (len(array) >= 4):
                    print(who + " won the game!")
                    return True
                    break    
            else:
                array = []

    #diagonal
    for column in range(length):
        array = []
        if (column <= length - 4):
            for row in range(height):
                spot = field[height - 1 - row][column + len(array)]
                if (spot != "_"):
                    if (len(array) == 0):
                        array.append(spot)
                    elif (spot == array[len(array) - 1]):
                        array.append(spot)
                    else:
                        array = [spot]

                    if (len(array) >= 4):
                        print(who + " won the game!")
                        return True
                        break
                else:
                    array = []
    

while True:
    win = False

    field = []
    for i in range(height):
        field.append(["_"]*length)

    if (height < 4 and length < 4):
        print("The field is smaller than a 4x4 making the game impossible.")
        break

    while win == False:
        buildField(field)
        if (checkForWin(field,enemy) == True):
            win = True
            break
        turn(player)
        buildField(field)
        if (checkForWin(field,player) == True):
            win = True
            break
        turn(enemy)
