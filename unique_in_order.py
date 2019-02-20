def unique_in_order(iterable):
    arr = list(iterable)
    new_arr = []
    if len(arr) == 0:
        return new_arr
    else:
        new_arr.append(arr[0])
        for k in range(1,len(arr),1):
            #If the last element in the new array matches that with the current element being looked at, it is a repeat
            if arr[k] != new_arr[len(new_arr)-1]:
                new_arr.append(arr[k])
    return new_arr
