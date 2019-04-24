import math

def base_conversion(x, arr):
    if x > 255:
        arr.append('F')
        arr.append('F')
    elif x <= 0:
        arr.append('0')
        arr.append('0')
    elif math.floor(x/16) == 0:
        arr.append('0')
    elif math.floor(x/16) == 1:
        arr.append('1')
    elif math.floor(x/16) == 2:
        arr.append('2')
    elif math.floor(x/16) == 3:
        arr.append('3')
    elif math.floor(x/16) == 4:
        arr.append('4')
    elif math.floor(x/16) == 5:
        arr.append('5')
    elif math.floor(x/16) == 6:
        arr.append('6')
    elif math.floor(x/16) == 7:
        arr.append('7')
    elif math.floor(x/16) == 8:
        arr.append('8')
    elif math.floor(x/16) == 9:
        arr.append('9')
    elif math.floor(x/16) == 10:
        arr.append('A')
    elif math.floor(x/16) == 11:
        arr.append('B')
    elif math.floor(x/16) == 12:
        arr.append('C')
    elif math.floor(x/16) == 13:
        arr.append('D')
    elif math.floor(x/16) == 14:
        arr.append('E')
    else:
        arr.append('F')
    subtract_off = 16*math.floor(x/16)
    new_num = x - subtract_off
    if x < 256 and x > 0:
        if new_num == 0:
            arr.append('0')
        elif new_num == 1:
            arr.append('1')
        elif new_num == 2:
            arr.append('2')
        elif new_num == 3:
            arr.append('3')
        elif new_num == 4:
            arr.append('4')
        elif new_num == 5:
            arr.append('5')
        elif new_num == 6:
            arr.append('6')
        elif new_num == 7:
            arr.append('7')
        elif new_num == 8:
            arr.append('8')
        elif new_num == 9:
            arr.append('9')
        elif new_num == 10:
            arr.append('A')
        elif new_num == 11:
            arr.append('B')
        elif new_num == 12:
            arr.append('C')
        elif new_num == 13:
            arr.append('D')
        elif new_num == 14:
            arr.append('E')
        else:
            arr.append('F')


def rgb(r, g, b):
    arr = []
    base_conversion(r, arr)
    base_conversion(g, arr)
    base_conversion(b, arr)
    str1 = ''.join(arr)
    return str1

rgb(254, 254, 300)
