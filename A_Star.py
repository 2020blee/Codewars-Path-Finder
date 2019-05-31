#I am stuck in an infinite loop somewhere but I don't know why

import math

def astar(graph):
    #Nodes that have been discovered
    discovered = []
    #Hash storing costs
    g_hash = {}
    #Hash storing distance
    h_hash = {}

    #First, we establish values for 0,0 in the hashes
    g_hash[(0,0)] = 0
    h_hash[(0,0)] = math.sqrt((len(graph)-2)**2 + (len(graph[0])-2)**2)

    #We add 0,0 to our discovered nodes
    discovered.append([0,0])

    #We stop when we find [-1,-1]
    while [len(graph)-1,len(graph)-1] not in discovered:
        #px,py will store the value of the coordinates of the node with the shortest g_score + h_score, meaning we should check it with priority
        px,py = 0,0
        #King of the hill algorithm
        for [x,y] in discovered:
            if g_hash[(x,y)] + h_hash[(x,y)] < g_hash[(px,py)] + h_hash[(px,py)]:
                px,py = x,y

        #i,j will store the original values of px,py because we will change px,py
        i,j = px,py

        #px,py will check to the right and down
        for px,py in (px+1,py),(px,py+1):
            if 0 <= px < len(graph) and 0 <= py < len(graph[0]):
                if [px,py] not in discovered:
                    discovered.append([px,py])
                #Calculates g_score and h_score to be stored in the hash
                g_score = abs(graph[px][py] - graph[i][j]) + g_hash[(i,j)]
                g_hash[(px,py)] = g_score
                h_score = math.sqrt((len(graph) - px - 2)**2 + (len(graph[0]) - py - 2)**2)
                h_hash[(px,py)] = h_score


    print(g_hash[(len(graph)-1, len(graph)-1)])

graph = [[0, 6, 6, 2, 8, 9, 9, 3, 8, 3],
 [6, 5, 2, 9, 5, 7, 9, 1, 7, 7],
 [3, 9, 5, 1, 4, 3, 0, 1, 8, 3],
 [4, 7, 2, 6, 4, 8, 0, 2, 9, 2],
 [3, 5, 0, 6, 0, 1, 1, 2, 6, 9],
 [9, 8, 5, 8, 3, 2, 4, 9, 9, 0],
 [9, 7, 7, 9, 1, 1, 5, 0, 2, 5],
 [1, 4, 4, 3, 3, 4, 1, 9, 4, 4],
 [5, 5, 2, 0, 9, 6, 2, 7, 3, 3],
 [8, 2, 4, 8, 2, 2, 2, 3, 1, 6]]

astar(graph)
