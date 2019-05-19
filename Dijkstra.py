#Used this source to help me understand the algorithm: https://www.youtube.com/watch?v=IG1QioWSXRI
#Used this source to help me assign the nodes in the graph values in the hash and modify them accordingly: https://thispointer.com/python-how-to-add-append-key-value-pairs-in-dictionary-using-dict-update/
#Also, used this source: https://www.tutorialspoint.com/python/dictionary_get.htm

def path_finder(area):

    area = list(map(list, area.splitlines()))


    #Queue that keeps track of any nodes that we haven't explored yet
    unexplored = []

    #Hash that displays whether each node has been explored at all or not
    visited = {}

    #Hash to display the cost for each node. The values are subject to change as we explore the array
    cost = {}

    #Sends all the nodes to the unexplored array when we start out
    for x in range(len(area)):
        for y in range(len(area)):
            unexplored.append([x,y])

    #For every node in the matrix, we have it set to not explored by default
    for [x,y] in unexplored:
        visited[(x,y)] = False

    #We set every node in the matrix to zero cost by default.
    for [x,y] in unexplored:
        cost[(x,y)] = 0

    #This while loop remains active until all nodes are explored
    while unexplored:
        #Removes the node and assigns the coordinates as x,y
        x,y = unexplored.pop(0)

        #i,j stores the coordinates of the original node, while x,y will vary with the for loop
        i,j = x,y
        #Marks the current node that has just been taken out from the queue as explored
        visited[(x,y)] = True
        #x,y will represent all the different adjacent nodes from i,j
        for x,y in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
            #This is to prevent the nodes from going out of the boundaries of the matrix
            if 0 <= x < len(area) and 0 <= y < len(area[0]):
                #The new candidate for the cost takes the absolute value between the two adjacent nodes and adds it to the cost of the original node
                new_cost = abs(int(area[i][j]) - int(area[x][y])) + cost.get((i,j))
                #The only times we update the cost of a node is if we realize it is not checked or if we find that the new candidate of the cost is cheaper than the current cost
                if visited.get((x,y)) == False or new_cost < cost.get((x,y)):
                    cost[(x,y)] = new_cost

    return cost.get((len(area)-1,len(area)-1))
