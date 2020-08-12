# Our maze explorer has some weird rules for finding the exit. It is up to you find out if it is possible with the following rules, whether they will escape.

# Our explorer has the following rules:
# •	They always walk 6 blocks straight and then turn 180° and start walking 6 blocks again.
# •	If a wall is in their way they turn to the right, if that not possible they turn to the left and if that is not possible, they turn back from where they came.

# Legend:
# >: Explorer looking East
# <: Explorer looking West
# ^: Explorer looking North
# v: Explorer looking south
# E: Exit
# #: wall
#  : Clear passage way (empty space)




#First make a maze, each nested list is a row in the maze.

grid = [["#"," ",">", " ", " "," ", " "," "," "]]


#Get the explorer to start walking in one direction according to it's starting position:

def walkForward():
    def gridPos():
        for row in grid:
            for n in row:
                if n != "#" and n != " " and n != "E":
                    gridPosition = grid.index(row)
                    return gridPosition

    def rowPos():
        for row in grid:
            for n in row:
                if n != "#" and n != " " and n != "E":
                    rowPosition = row.index(n)
                    return rowPosition
    gridPosition = gridPos()
    rowPosition = rowPos()                    
    iterator = 1


    while rowPosition < 8:   
        if grid[gridPosition][rowPosition+1] == " ":
                if iterator <7:
                    print("row position: ", rowPosition)
                    # Stop the explorer from moving more than 6 steps forward
                    # Stop the explorer from moving outside of nested list len                              
                    grid[gridPosition][rowPosition] = " "
                    grid[gridPosition][rowPosition+1] = ">"
                    rowPosition = rowPos()
                    gridPosition = gridPos() 
                    print(grid)
                    iterator +=1
    else:
                    iterator = 1
                    while rowPosition >= 0:
                        if grid[gridPosition][rowPosition-1] == " ":
                            grid[gridPosition][rowPosition] = " "
                            grid[gridPosition][rowPosition-1] = "<"
                            rowPosition = rowPos()
                            gridPosition = gridPos()
                            iterator +=1
                        else:
                            break    
     
            # If the explorer has moved 6 steps forward they turn around



walkForward()