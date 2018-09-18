array = [2 ,3 ,4 ,12 ,40 ,90]
search_element = int(input("Enter Number to be searched "))

def binary_search(array, lower, higher, search_element):
    if lower <= higher:
        mid = (lower + higher ) // 2
        if array[mid] == search_element:
            print("Element {} found at position {}".format(search_element, mid))
            exit()
        elif(search_element < array[mid]):
            binary_search(array, lower, mid-1, search_element)
        else:
            binary_search(array, mid+1, higher, search_element)
    else:
        print("Element not found in array")

def main():
    binary_search(array, lower=0, higher=len(array)-1, search_element=search_element)

if __name__ == '__main__':
    main()