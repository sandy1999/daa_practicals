array  = [4,5,3,1,2,6]

print("Intermediate steps of array sorting")
for i in range(len(array)):
    for j in range(i+1,len(array)):
        if(array[j] < array[i]):
            array[i], array[j] = array[j], array[i]
        print("Pass {} sorted array {} ".format(i,array))
print("Array after completely sorting")
print(array)