def binarySearch(alist, item):
    first = 0
    last = len(alist)-1
    found = False
    while first<=last and not found:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            print("Element found at postion {}".format(midpoint))
            exit()
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    print("Element not found in array")
testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
binarySearch(testlist, 3)
binarySearch(testlist, 13)