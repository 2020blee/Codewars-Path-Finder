def path_finder(maze):
    #This organizes the matrix better
    maze = [list(level) for level in maze.split("\n")]

    #Array to hold all the vertices that need to be inspected for undiscovered neighboring vertices
    vertices = []

    #Array to hold the vertices that have been inspected
    checked_vertices = []

    #Covering the case where the starting vertex is impassible
    if maze[0][0] == 'W':
        return False

    #Otherwise, we start inspecting at 0,0 and try to find if (n-1),(n-1) is accessible
    else:
        vertices.append([0,0])

    #This function inspects the vertices in the vertices array, finds the undiscovered vertices, and then sends the inspected vertex to the checked_vertices array
    #This function is a BFS in a way because it checks for new vertices from each vertex in a set without going back a level
    def find_vertices(matrix):
        for [x, y] in vertices:
            k = len(vertices)
            #Checks east
            if 0 <= x < len(matrix) and 0 <= y+1 < len(matrix):
                #Only vertices that are not up for inspection or are already inspected should be added to the vertices array. We don't want repeats
                if matrix[x][y+1] == '.' and [x,y+1] not in vertices and [x,y+1] not in checked_vertices:
                    vertices.append([x,y+1])
            #Checks south
            if 0 <= x+1 < len(matrix) and 0 <= y < len(matrix):
                if matrix[x+1][y] == '.' and [x+1,y] not in vertices and [x+1,y] not in checked_vertices:
                    vertices.append([x+1,y])
            #Checks west
            if 0 <= x < len(matrix) and 0 <= y-1 < len(matrix):
                if matrix[x][y-1] == '.' and [x,y-1] not in vertices and [x,y-1] not in checked_vertices:
                    vertices.append([x,y-1])
            #Checks north
            if 0 <= x-1 < len(matrix) and 0 <= y < len(matrix):
                if matrix[x-1][y] == '.' and [x-1,y] not in vertices and [x-1,y] not in checked_vertices:
                    vertices.append([x-1,y])
            #The vertex has been inspected in each cardinal direction, so we can change the array it is in
            vertices.remove([x,y])
            checked_vertices.append([x,y])


    #This function keeps checking the maze until it is sure all vertices that are reachable have been covered
    def mass_checker(maze):
        #This stores how many vertices have been checked already before the maze is checked
        g = len(checked_vertices)
        find_vertices(maze)
        #If it finds that new vertices have been found after the check, the mass checker runs again
        if len(checked_vertices) != g:
            mass_checker(maze)
        #If no new vertices are found, we reached the highest level in the BFS and we can stop. We then check if the lower right element is present in the checked vertices or not
        else:
            if [len(maze)-1, len(maze)-1] in checked_vertices:
                return True
            else:
                return False

    mass_checker(maze)
