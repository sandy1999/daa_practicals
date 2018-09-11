array = [2 ,3 ,4 ,10 ,40 ,90]
search_element = int(input("Enter Number to be searched "))
l = 0
h = len(array) -1 

while (l < h):
    mid = int(l + (h-l)/2)
    
    if array[mid] == array[mid]:
        print("Element {} found at position {}".format(search_element, mid))
        exit()
    elif array[mid] < search_element:
        l = mid + 1
    else:
        h = mid - 1
print("Element {} not found in array".format(search_element))