#https://www.programiz.com/python-programming/nested-dictionary (This helped with accessing values in nested dictionaries)

#Dictionary to store what we believe to be the cheapest cost to get to a particular node. The values will be updated as we go
cost_hash = {}

def bellman_ford(graph, start):

    #We first set every node's cost at to be determined for now
    for vertex in graph:
        cost_hash[str(vertex)] = "TBD"

    #The starting node (whatever it is) will have cost 0
    cost_hash[str(start)] = 0

    #This for loop ensures the minimum number of times to go through the graph to guarantee that the cheapest costs will be correct. Each time, we guarantee at least one node will have the correct cheapest cost, which is why it takes N - 1 times, since the starting node's cost is fixed at 0
    for i in range(0,len(graph)-1):
        #Each cycle, we loop through each vertex
        for vertex in graph:
            #This edge for loop taps into the dictionary inside the dictionary in the graph to access edge weights
            for edge in graph[str(vertex)]:
                #We can only progress if the vertex we have chosen actually has a determined cost
                if cost_hash[str(vertex)] != "TBD":
                    #This new_candidate variable will help us keep track of what could overtake the current cost in the cost_hash
                    new_candidate = graph[str(vertex)][str(edge)] + cost_hash[str(vertex)]
                    #If we determine the cost of the vertex at the other end of the edge is not determine, we change it.
                    if cost_hash[str(edge)] == "TBD":
                        cost_hash[str(edge)] = new_candidate
                    #Otherwise, we compare prices and determine if we need to update the price
                    elif new_candidate < cost_hash[str(edge)]:
                        cost_hash[str(edge)] = new_candidate

    print(cost_hash)

graph = {
           's': {'a': 3, 'b': -1},
           'a': {'s': 4, 'b': 4, 'c':8},
           'b': {'s': 1, 'a': 2, 'd': 2},
           'c': {'a': 2, 'd': 7, 't': 4},
           'd': {'b': 1, 'c': 11, 't': 5},
           't': {'c': 3, 'd': 5}
           }

bellman_ford(graph, 'a')
