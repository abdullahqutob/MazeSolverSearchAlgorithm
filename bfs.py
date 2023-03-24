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

# BFS Function
def bfs(maze):

    start, end = base.findStartEnd(maze) # Get start and end points

    # No start or end found
    if start is None or end is None:
        raise ValueError("Missing start or end")

    # Queue with start point added
    queue = Queue()
    queue.put(start)

    # Keeping track of visited nodes
    visited = set()
    visited.add(start)

    # Keep track of each nodes' parents | key = node, value = parent node
    parents = {start: None}

    # Counter for the number of visited nodes
    visitedCounter = 0    
   
    while queue:
        # Dequeue the next point from the queue
        current = queue.get()
        if current == end:
            result = [] # Final path
            while current != start:
                result.append(current) # add to result list
                current = parents[current] # reconstruct path
            # Add start point to path list and reverse list order
            result.append(start)
            result.reverse()
            # Return the path and the number of visited nodes
            return result, visitedCounter
        
        # Otherwise, add its neighbors to the queue
        for neighbor in getNeighbors(current, maze):
            if neighbor not in visited:
                visited.add(neighbor)
                parents[neighbor] = current
                queue.put(neighbor)
                visitedCounter += 1

    # If theres no path
    return "No path found", visitedCounter



if __name__ == '__main__':
       
    mazeFile = input("Enter maze file path: ") # Get the maze file path from the user
    
    maze = base.readMazeFile(mazeFile) # Read and process the maze fileF
    
    startTime = time.perf_counter() # Start timer
   
    path, visitedCounter = bfs(maze) # Run bfs algorithm

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
    base.writePathFile(path, "BFS", mazeFile)