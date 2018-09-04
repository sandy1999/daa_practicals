array  = [4,5,3,1,2,6]

print("Intermediate steps of array sorting")
for i in range(1,len(array)):
    pivot = array[i]
    j = i-1
    # print(pivot, j)
    while j >= 0 and pivot < array[j]:
        array[j+1] = array[j]
        j-=1
    array[j+1] = pivot
    print("Pass {} sorted array {} ".format(i,array))
print("Array after completely sorting")
print(array)