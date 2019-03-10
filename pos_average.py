def pos_average(s):
    substrings = s.split(", ")
    matches = 0
    total_combinations = 0
    for x in range(len(substrings)-1):
        for y in range(x+1,len(substrings)):
            for z in range(len(substrings[x])):
                if substrings[x][z] == substrings[y][z]:
                    matches += 1
                total_combinations += 1
    answer = matches / total_combinations * 100
    print(answer)
