array = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
first = 0
last = len(array)-1
found = False
item = int(input("Enter element to be searched in array "))
while first<=last and not found:
    midpoint = (first + last)//2
    if array[midpoint] == item:
        print("Element found at postion {}".format(midpoint))
        exit()
    else:
        if item < array[midpoint]:
            last = midpoint-1
        else:
            first = midpoint+1
print("Element not found in array")