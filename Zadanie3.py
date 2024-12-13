import random

#1

arr1 = [3,7,1,0,4]
arr2 = [[2,3],[7,1],[0,4]]
arr3 = [7 for i in range(5)]
arr4 = [i for i in range(1,10)]
arr5 = [i*2 for i in range(1,10)]
arr6 = [random.randint(1,20) for i in range(10)]
arr7 = [[] for i in range(5)]
arr8 = [[1 for i in range(2)] for j in range(4)]
arr9 = [[random.randint(1,20) for i in range(3)] for j in range(5)]
#an array with values: 4,0,3
arr10 = [4, 0, 3]
#15-element array filled with zeros
arr11 = [0 for i in range(15)]
#an array with integer values in the range of <1,30>
arr12 = [x for x in range(1, 31)]
#20-element array filled with 0 or 1 randomly
arr13 = [random.randint(0, 1) for x in range(20)]
#two dimensional array with five rows and two columns filled with False
arr14 = [[False for i in range(2)] for j in range(5)]
for collection in arr14:
    for words in collection:
        print(words, end=' ')
    print()

#2

arr1 = [34,7,19,4,21,8]
licznik = 0
suma = 0
while licznik < len(arr1):
    if arr1[licznik] % 2 == 0:
        suma += arr1[licznik]
    licznik += 1
print(suma)

#3

arr1 = [15, 8, 31, 47, 2, 19]
print('Existed array:', end=' ')
for x in arr1:
    print(x, end=' ')
print()
print('Reversed array:', end=' ')
for x in reversed(arr1):
    print(x, end=' ')

#4

arr = [-15, 8, -31, 47, -2, 19]
max_num = 0
min_num = 0
for x in arr:
    if x > max_num:
        max_num = x
    if x < min_num:
        min_num = x
print('Max number is: ',max_num)
print('Min number is: ',min_num)

#5

arr = [15, 8, 31, 47, 2, 19]
total = 0
for x in arr:
    total += x
srednia = total / len(arr)
print(f'Średnia wynosi: {round(srednia, 2)}')

#6

arr = [15, 8, 31, 47, 2, 19]
total = 0
licznik = 0
while licznik < len(arr):
    total += arr[licznik]
    licznik += 1
srednia = total / len(arr)
print(f'Średnia wynosi: {round(srednia, 2)}')

#7

arr = ['Genowefa', 'Onufry', 'Celestyna', 'Alojzy', 'Pankracy']
longest_name = ''
for x in arr:
    if len(x) > len(longest_name):
        longest_name = x
print('Longest name is: ', longest_name)

#8

arr = [2, 6, 4, 9, 7]
def star(n):
    return '*' * n
licznik = 0
while licznik < len(arr):
    print(f'{arr[licznik]}: {star(arr[licznik])}')
    print()
    licznik += 1

#9

def compare(array1, array2):
    if len(array1) != len(array2):
        return False
    else:
        licznik = 0
        for x in array1:
            if x == array2[licznik]:
                licznik += 1
            else:
                return False
        if licznik == len(array1):
            return True
        
arr1 = ["water","book","sky"]   
arr2 = ["water","book","sky"]
arr3 = [True,False]   
arr4 = [True,False,True]
arr5 = [5,3,1] 
arr6 = [5,3,1]
arr7 = [3,2,1]
arr8 = [3,2]

print(f'Statement that {arr1} and {arr2} are the same is: ', compare(arr1, arr2))
print(f'Statement that {arr3} and {arr4} are the same is: ', compare(arr3, arr4))
print(f'Statement that {arr5} and {arr6} are the same is: ', compare(arr5, arr6))
print(f'Statement that {arr7} and {arr8} are the same is: ', compare(arr7, arr8))

#10

arr1 = [4,36,12,28,9,44,5]
arr2 = [5,1,36]
for x in arr1:
    if not x in arr2:
        print(x)

#11

def bubbbleSort(array):
    n = len(array)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array
arr1 = [4, 32, 7, 15, 2, 102, -6, 5, -17]
arr2 = [4, 36, 12, 28, 9, 44, 5]
arr3 = [-15, 8, -31, 47, -2, 19]

print(f'Array 1: {arr1}')
print(f'Array 2: {arr2}')
print(f'Array 3: {arr3}')

bubbbleSort(arr1)
bubbbleSort(arr2)
bubbbleSort(arr3)

print(f'Sorted array 1: {arr1}')
print(f'Sorted array 2: {arr2}')
print(f'Sorted array 3: {arr3}')

#12

arr1 = [2, 3, 2, 5, 8, 1, 9, 8]
arr2 = []
print('Array:', end=' ')
for x in arr1:
    if not x in arr2:
        arr2.append(x)
    print(x, end=' ')
print()
print('Unique:', end=' ')
for y in arr2:
    print(y, end=' ')

#13

def occurs(number, array):
    if number in array:
        return True
arr1 = [15, 38, 7, 23, 14]
number_given = int(input('Enter number: '))
if occurs(number_given, arr1):
    print(f'Number {number_given} occurs in array')
else:
    print(f'Number {number_given} doesnt occurs in array')

#15

tup = (10,20,30,40,50)
reversed_tup = tup[::-1]
print('Tuple:',end=" ")
for x in tup:
    print(x, end=" ")
print()
print('Reversed order:', end=' ')
for x in reversed_tup:
    print(x, end=' ')

#16

tup = ("Seven", [10, 20, 30], (5, 15, 25))

print(tup[0])

print(max(tup[1]))

#17

my_tuple = (50, 20, 40, 50, 30, 50)
value_to_count = 50

occurrences = my_tuple.count(value_to_count)

print(f'Tuple: {my_tuple}')
print(f'Value: {value_to_count}')
print(f'Number of occurrences: {occurrences}')

#18

import MyArrays

arr1 = [7,3,8,5,2]
print('Numbers: ', end=' ')
for x in arr1:
    print(x, end=' ')
print()
print(f'Second largest number: {MyArrays.second_largest(arr1)}')
print(f'Median: {MyArrays.median(arr1)}')
print(f'Smallest and largest number: {MyArrays.create_arr_min_max(arr1)}')
print(f'Numbers as a string:', end=' ')
MyArrays.string_element(arr1)


#19

arr1 = [15, 8, 31, 47, 2, 19]
arr2 = []
number = int(input('Enter a number: '))
for x in arr1:
    if x > number:
        print(x, end=' ')

#20

arr = [7,9,2,4,5,6]
n = len(arr)
for i in range(n - 1):
    for j in range(n - i - 1):
        if (arr[j]%2) > (arr[j+1]%2):
            arr[j], arr[j+1] = arr[j+1], arr[j]
print(arr)

#21

def is_subset(arr1, arr2):
    # Check if every element in arr1 exists in arr2
    for element in arr1:
        if element not in arr2:
            return False
    return True

# Example usage
arr1 = [1, 2, 3]
arr2 = [3, 2, 1, 4, 5]

# Check if arr1 is a subset of arr2
if is_subset(arr1, arr2):
    print(f'{arr1} is a subset of {arr2}')
else:
    print(f'{arr1} is NOT a subset of {arr2}')

#22

import random

# Define the function that returns a randomly selected element from the array
def rand_elem(array):
    return random.choice(array)

# Example usage with a few randomly selected elements
arr = [10, 20, 30, 40, 50]

# Print a few randomly selected array elements
print(rand_elem(arr))
print(rand_elem(arr))
print(rand_elem(arr))

#23

import MyText  # Import the MyText module

# Sample text
text = "An apple a day keeps the doctor away"

# Call functions from MyText and print results
print(f"Text: {text}")
print(f"Number of words: {MyText.count_words(text)}")

print("Words from the longest to shortest:", ", ".join(MyText.longest_to_shortest(text)))
print("Words ordered alphabetically:", ", ".join(MyText.alphabetically_ordered(text)))

#24

import matplotlib.pyplot as plt
xpoints = [1, 8]
ypoints = [3, 10]
plt.plot(xpoints, ypoints)
plt.show()

#25

import matplotlib.pyplot as plt

x = []
y = []

for n in range(-100, 101):
    x.append(n)
for n in x:
    y.append(n**2 - 3)
plt.plot(x, y, label='f(x)= x^2 - 3')
plt.title('f(x)= x^2 - 3')
plt.grid()
plt.show()

#26

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 360, 1000)
y = np.sin(np.radians(x))

plt.plot(x, y, label='sin(x)', color = 'blue')
plt.title('sin(x)', color = 'red')
plt.grid()
plt.show()

#27

array = [
    [10, 20, 30, 40],
    [50, 60, 70, 80]
]

print("Array values:")
for row in array:
    for value in row:
        print(value, end=' ')
    print() 

#28

array = [
    [7, 3, 7, 9, 0],
    [2, 9, 0, 1, 5],
    [3, 8, 6, 4, 7],
    [8, 7, 1, 1, 5]
]

sum_last_column = 0

for row in array:
    sum_last_column += row[-1] 

print("Sum of values in the last column:", sum_last_column)

#29

def create_2d_arr(x, y):
    return [[0 for _ in range(y)] for _ in range(x)]

array = create_2d_arr(3, 5)

for row in array:
    print(row)

#30

array = [[0 for _ in range(5)] for _ in range(5)]

for i in range(1, 6): 
    for j in range(1, 6): 
        array[i - 1][j - 1] = i * j

for row in array:
    print(" ".join(str(value) for value in row))

#31

array = [[-38, 19], [5, 40], [-7, 11], [29, 16]]

min_value = array[0][0]
max_value = array[0][0]
min_position = (0, 0)
max_position = (0, 0)

for i in range(len(array)):
    for j in range(len(array[i])):
        if array[i][j] < min_value:
            min_value = array[i][j]
            min_position = (i, j)
        if array[i][j] > max_value:
            max_value = array[i][j]
            max_position = (i, j)

print(f"Smallest value: {min_value} at row {min_position[0]}, column {min_position[1]}")
print(f"Largest value: {max_value} at row {max_position[0]}, column {max_position[1]}")

#32

array = [
    [1, 2, 3, 4, 5], 
    [6, 7, 8, 9, 10], 
    [11, 12, 13, 14, 15] 
]

def print_array(arr):
    for row in arr:
        print(" ".join(map(str, row)))
    print()

print("Array before swapping:")
print_array(array)

array[0], array[-1] = array[-1], array[0]

print("Array after swapping:")
print_array(array)

#33

array = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15] 
]

def print_array(arr):
    for row in arr:
        print(" ".join(map(str, row)))
    print()

print("Array before swapping:")
print_array(array)

for row in array:
    row[0], row[-1] = row[-1], row[0]

print("Array after swapping:")
print_array(array)

#34

def identity_matrix(n):
    matrix = [[0] * n for _ in range(n)]
    
    for i in range(n):
        matrix[i][i] = 1
    
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

for size in [3, 5, 8]:
    print(f"Identity Matrix of size {size}:")
    matrix = identity_matrix(size)
    print_matrix(matrix)
    print() 

#35

def transpose_matrix(m):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

matrices = [
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[1, 2, 3, 4, 5], [6, 7, 8, 9, 0], [5, 6, 7, 8]] 
]

for matrix in matrices:
    print("Original Matrix:")
    print_matrix(matrix)
    print("Transposed Matrix:")
    transposed = transpose_matrix(matrix)
    print_matrix(transposed)
    print() 

#36

def convert_to_1d(arr_2d):
    return [element for row in arr_2d for element in row]

def print_array(arr_1d):
    print(arr_1d)

arrays_2d = [
    [[2, 3], [1, 5]],
    [[5, 0, 3, 7, 5], [9, 0, 9, 1, 2]],
    [[2, 1], [3, 5], [7, 4], [2, 6]]
]

for arr_2d in arrays_2d:
    print("Original 2D array:")
    for row in arr_2d:
        print(row)
    print("Converted 1D array:")
    arr_1d = convert_to_1d(arr_2d)
    print_array(arr_1d)
    print()
