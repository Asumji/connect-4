#config
player = "\x1b[32mO\x1b[0m"
enemy = "\x1b[31mO\x1b[0m"


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
            if (int(i) <= 7 and int(i) >= 0):
                if (field[0][int(i) - 1] == "_"):
                    for j in range(6):
                        row = field[j]
                        if (row[int(i) - 1] != "_"):
                            field[j - 1][int(i) - 1] = who
                            turnActive = False
                            break
                        elif (j == 5):
                            row[int(i) - 1] = who 
                            turnActive = False
                else:
                    print("That column is full!")
            else:
                print("Enter a number 1 - 7.")
        else:
            print("Enter a number 1 - 7.")

def checkForWin(gamefield, who):
    #horizontal
    for row in gamefield:
        if (row[0] == who and row[1] == who and row[2] == who and row[3] == who or row[3] == who and row[4] == who and row[5] == who and row[6] == who or row[1] == who and row[2] == who and row[3] == who and row[4] == who or row[2] == who and row[3] == who and row[4] == who and row[5] == who):
            print(who + " won the game!")
            return True
    
    #vertical
    for column in range(6):
        array = ["","","","","",""]
        for j in range(6):
            if (field[j][column] != "_"):
                array[j] = field[j][column]
        if (array[1] == who and array[2] == who and array[3] == who and array[4] == who or array[0] == who and array[1] == who and array[2] == who and array[3] == who or array[5] == who and array[4] == who and array[3] == who and array[2] == who):
            print(who + " won the game!")
            return True

    #diagonal
    array = []
    array2 = []
    count = 0
    for row in range(6):
        for spot in range(7):
            count += 1 
            if (len(gamefield) * 7 >= count + 21):
                array.append(gamefield[row][spot])

    for row in gamefield:
        for spot in row:
            array2.append(spot)    

    rowSpot = -1
    for spot in range(len(array)):
        rowSpot += 1

        if (rowSpot <= 3):
            if (array2[spot] == who and array2[spot + 8] == who and array2[spot + 16] == who and array2[spot + 24] == who):
                print(who + " won the game!")
                return True
        if (rowSpot >= 3):
            if (array2[spot] == who and array2[spot + 6] == who and array2[spot + 12] == who and array2[spot + 18] == who):
                print(who + " won the game!")
                return True
        if (rowSpot == 6):
            rowSpot = -1
    

while True:
    win = False

    field = [
        ["_","_","_","_","_","_","_"],
        ["_","_","_","_","_","_","_"],
        ["_","_","_","_","_","_","_"],
        ["_","_","_","_","_","_","_"],
        ["_","_","_","_","_","_","_"],
        ["_","_","_","_","_","_","_"],
    ]

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
    
