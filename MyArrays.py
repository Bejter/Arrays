def second_largest(arr): #A function that returns the second largest element in an array
    largest = 0
    second = 0
    for num in arr:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num
    return second

def min_max_diff(arr): #A function that returns the difference between the largest and smallest values in an array
    maxi = arr[0]
    mini = arr[0]
    for x in arr:
        if x > maxi:
            maxi = x
        elif x < mini:
            mini = x
    diff = maxi - mini
    return diff

def median(arr): #A function that returns the median of numbers in an array
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    if n // 2:
        return arr[n // 2]
    else:
        mid1 = arr[n // 2 - 1]
        mid2 = arr[n // 2]
        return (mid1 + mid2) / 2

def create_arr_min_max(arr):
    maxi = arr[0]
    mini = arr[0]
    for x in arr:
        if x > maxi:
            maxi = x
        elif x < mini:
            mini = x
    arr1 = [mini, maxi]
    return arr1

def string_element(arr):
    for x in arr:
        if arr.index(x) < len(arr) - 1:
            print(f'{str(x)}',end='-')
        else:
            print(f'{str(x)}')