array = [[0 for _ in range(5)] for _ in range(5)]

for i in range(1, 6): 
    for j in range(1, 6): 
        array[i - 1][j - 1] = i * j

for row in array:
    print(" ".join(str(value) for value in row))
