import os

# Removes spaces and converts maze into list of characters
def formatMazeLine(line):
    return [c for c in line if c != ' ']

# Reads a maze file and returns the maze as a 2D array
def readMazeFile(file):
    filePath = "mazes/" + file
    with open(filePath, 'r') as f:
        maze = [formatMazeLine(line.rstrip()) for line in f]
    # Remove empty lines at the end of the file
    while maze and not maze[-1]:
        maze.pop()
    return maze

# Finds the start and end indexes
def findStartEnd(maze):
    start = None
    end = None
    
    # Start index at first line
    for i in range(len(maze[0])):
        if maze[0][i] == '-':
            start = (0,i)

    # End index at last line
    for i in range(len(maze[0])):
        if maze[len(maze) -1][i] == '-':
            end = (len(maze)-1,i)
    
    return start, end

# Converts path from list of indexes to string of movements
def pathInLetters(path):
    pathLetters = []
    for i in range(1, len(path)):
        diffY = path[i][0] - path[i-1][0]
        diffX = path[i][1] - path[i-1][1]
        if abs(diffY) > 1 or abs(diffX) > 1: # If any skips or jumps have been made
            pathLetters.append('X')
        if diffY == 1: # Move down
            pathLetters.append('D')
        elif diffY == -1: # Move up
            pathLetters.append('U')
        elif diffX == 1: # Move right
            pathLetters.append('R')
        elif diffX == -1: # Move left
            pathLetters.append('L')
    return ''.join(pathLetters)



def writePathFile(path, search, mazeFile):

    # If path file does not exist, create it
    if not os.path.exists("Paths"):
        os.makedirs("Paths")

    outputFile = "Paths/" + search + "-" + mazeFile 

    # Creates the output file in write mode and writes the path
    with open(outputFile, "w") as f:
        f.write(str(path) + "\n\n" + str(pathInLetters(path)))