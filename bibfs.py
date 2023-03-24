import time
from queue import Queue
import base

# Returns a list of valid neighbors for the given node
def getNeighbors(node, maze):
    neighbors = []
    row, col = node
    if row > 0 and maze[row-1][col] != '#': # up
        neighbors.append((row-1, col))
    if row < len(maze)-1 and maze[row+1][col] != '#': # down
        neighbors.append((row+1, col))
    if col > 0 and maze[row][col-1] != '#': # left
        neighbors.append((row, col-1))
    if col < len(maze[0])-1 and maze[row][col+1] != '#': # right
        neighbors.append((row, col+1))
    return neighbors
    
# Combines paths from start and end to the common node
def combinePaths(startPath, endPath, commonNode):
    path = []
    while commonNode:
        path.append(commonNode)
        commonNode = startPath.get(commonNode)
    path.reverse()
    commonNode = endPath.get(path[-1])
    while commonNode:
        path.append(commonNode)
        commonNode = endPath.get(commonNode)
    return path

# Bidirectional BFS Function
def bibfs(maze):
    
    start, end = base.findStartEnd(maze) # Get start and end points

    # No start or end found
    if start is None or end is None:
        raise ValueError("Missing start or end")
    
    # Visited set for start
    startVisited = set()
    startVisited.add(start)

    # Visited set for end
    endVisited = set()
    endVisited.add(end)
    
    # Queue for start and end
    startQueue = Queue()
    startQueue.put(start)
    endQueue = Queue()
    endQueue.put(end)

    # Path parent nodes of start and end
    startParents = {start: None}
    endParents = {end: None}
    
    # Counter for the number of visited nodes
    visitedCounter = 1
    
    while startQueue and endQueue:

        # Run BFS from the starting point
        startCurrent = startQueue.get()
        for neighbor in getNeighbors(startCurrent, maze):
            if neighbor not in startVisited:
                startVisited.add(neighbor)
                startParents[neighbor] = startCurrent
                startQueue.put(neighbor)
                
            # If common node is found -> return the combined path
            if neighbor in endVisited:
                path = combinePaths(startParents, endParents, neighbor)
                visitedCounter += len(startVisited) + len(endVisited)
                return path, visitedCounter
        
        # Run BFS from the ending point
        endCurrent = endQueue.get()
        for neighbor in getNeighbors(endCurrent, maze):
            if neighbor not in endVisited:
                endVisited.add(neighbor)
                endParents[neighbor] = endCurrent
                endQueue.put(neighbor)

            # If common node is found -> return the combined path
            if neighbor in startVisited:
                path = combinePaths(startParents, endParents, neighbor)
                visitedCounter += len(startVisited) + len(endVisited)
                return path, visitedCounter
    
    # If there is no path from start to end, return None and visited counter
    visitedCounter += len(startVisited) + len(endVisited)
    return "No path found", visitedCounter
    


if __name__ == '__main__':
       
    mazeFile = input("Enter maze file path: ") # Get the maze file path from the user
    
    maze = base.readMazeFile(mazeFile) # Read and process the maze fileF
    
    startTime = time.perf_counter() # Start timer
   
    path, visitedCounter = bibfs(maze) # Run bfs algorithm

    endTime = time.perf_counter() # End timer

    
    elapsedTime = endTime - startTime # Time elapsed

    # Print the path 
    print('Path: \n' + str(path))
    print("Path movements: \n" + str(base.pathInLetters(path)))
    
    
    # Print start and end points
    start, end = base.findStartEnd(maze)
    print("Start point: " + str(start))
    print("End point: " + str(end))
    
    # Print length of the path
    pathLength = len(path) -1
    print("Path Length: " + str(pathLength))

    # Print number of valid nodes in a maze
    numOfNodes = 0
    for line in maze:
        dashCount = line.count('-')
        numOfNodes += dashCount
    print("Maze length: " + str(numOfNodes))

    # Percent of nodes visited
    percentCoverage = (visitedCounter / numOfNodes) * 100 

    # Print number of nodes visited
    print("Nodes visited: " + str(visitedCounter) + " | " + str(percentCoverage) + "%")
    
    # Print elapsed time
    print("Elapsed time: " + str(elapsedTime) + " seconds")    

    # Write path to file
    base.writePathFile(path, "BiBFS", mazeFile)