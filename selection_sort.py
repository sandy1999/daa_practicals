array  = [4,5,3,1,2,6]

print("Intermediate steps of array sorting")
for i in range(len(array)):
    min_idx = i
    for j in range(i+1, len(array)):
        if(array[j] < array[min_idx]):
            min_idx = j
    array[i], array[min_idx] = array[min_idx], array[i]
    print("Pass {} sorted array {} ".format(i,array))
print("Array after completely sorting")
print(array)