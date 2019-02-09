def path_finder(maze):

    matrix = list(map(list, a.splitlines()))

    def find_edges(matrix):
        x,y = 0,0
        edges = []
        length = len(matrix)
        # add conditions for nw, sw, ne, se
        for x,y in (x, y+1), (x, y-1), (x+1, y), (x-1, y):
            if 0 <= x < length and 0 <= y < length:
                # check if matrix[x][y] is a free space
                if matrix[x][y] == '.':
                    edges.append([x,y])

    count = 0

    for x,y in edges:
        if [length-1][length-1] in edges:
            count += 1

    if count > 0:
        return True

    else:
        return False
