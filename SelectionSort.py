def SelectionSort(arr):
    for k in range(len(arr)):
        #Smallest element has index m
        m = k
        for n in range(m, len(arr), 1):
            if arr[n] < arr[m]:
                m = n
        arr[k], arr[m] = arr[m], arr[k]
    print(arr)

SelectionSort([15, 87, 23, 7, 56])
