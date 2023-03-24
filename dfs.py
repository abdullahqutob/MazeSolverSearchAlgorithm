import time
import base

# DFS Function
def dfs(maze):
    
    start, end = base.findStartEnd(maze) # Get start and end points

    # No start or end found
    if start is None or end is None:
        raise ValueError("Missing start or end")

    # Keeps track of visited nodes
    visited = set()
    # Stack to keep track of nodes left to explore
    unvisited = [start]
    #  Keep track of each nodes' parents | key = node, value = parent node
    parents = {start: None}
    
    # Counter for the number of visited nodes
    visitedCounter = 0

    # running dfs
    while unvisited:
        current = unvisited.pop()
        # If the current node is unvisited -> mark it as visited and add its neighbors to the unvisited stack
        if current not in visited:
            visited.add(current)
            visitedCounter += 1
            row, col = current
            # Order of visiting is reverse of the following order, because stack is last in first out
            neighbors = [(row-1, col), (row, col-1), (row, col+1), (row+1, col)] # Down, Right, Left, Up

            for neighbor in neighbors:
                neighborRow, neighborCol = neighbor
                # Check that neighboring nodes are not in the first row
                if neighborRow >= 0 and neighborRow < len(maze):
                    # Checking that neighboring nodes are within the side boundaries
                    if neighborCol >= 0 and neighborCol < len(maze[0]):
                        # Checking if node is valid path node
                        if maze[neighborRow][neighborCol] == '-':
                            # Checking if node is unvisited
                            if neighbor not in visited:
                                # Add it to the unvisited stack
                                unvisited.append(neighbor)
                                # Storing previous node | key = neighbor, value = current
                                parents[neighbor] = current
                
        # if current node is the exit -> return path
        if current == end:
            result = []

            # backtracks visited nodes and then reverses it to return path
            while current != None:
                result.append(current) # add to result list
                current = parents[current] # reconstruct path
            result.reverse()

            return result, visitedCounter

    return "No path found", visitedCounter




if __name__ == '__main__':
    
    mazeFile = input("Enter maze file path: ") # Get the maze file path from the user
    
    maze = base.readMazeFile(mazeFile) # Read and process the maze fileF
    
    startTime = time.perf_counter() # Start timer
   
    path, visitedCounter = dfs(maze) # Run bfs algorithm

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
    base.writePathFile(path, "DFS", mazeFile)