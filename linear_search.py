array = [1,4,15,3,2,90]

search_element = int(input("Enter element to be searched in an array "))

flag = 0

for element in array:
    
    if search_element == element :
        print("{} present in our array at position, {}".format(search_element, array.index(element)+1))
        exit()
print("Element not found in array")