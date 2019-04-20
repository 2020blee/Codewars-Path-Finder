def increment_string(str):
    k = 0
    ints = list("0123456789")
    if len(str) == 0:
        return "1"
    if str[len(str)-1] not in ints:
        str = str + '1'
        return str
    else:
        count = len(str)-1
        for x in str:
            if count == 0 and str[count] in ints:
                k = 0
                break
            elif count == 0 and str[count] not in ints:
                k = 1
                break
            elif str[count] in ints:
                count -= 1
            else:
                k = count + 1
                break

        part_1 = str[:k]
        num = str[k:]
        #Num is the number part of the string at the end
        num_int = int(num)

        #This gives an accurate number of the leading zeroes
        zeroes_count = 0
        for x in range(len(num)):
            if num[x] == '0':
                zeroes_count += 1
            else:
                break
        no_zeroes_num = num[zeroes_count:]

        decider = 0

        for x in range(len(no_zeroes_num)):
            if no_zeroes_num[x] != '9':
                decider = 1

        #Case 1: The number with leading zeroes stripped isn't just nines
        if decider == 1:
            new_num = num_int + 1
            part_2 = new_num.__str__()
            add_back_zeroes = 0
            #Add back any leading zeroes
            while add_back_zeroes < zeroes_count:
                part_1 = part_1 + '0'
                add_back_zeroes += 1
            return part_1 + part_2

        #Case 2: It is just a string of 9s
        else:
            #Case 2a: We have a consumable zero
            if zeroes_count > 0:
                zeroes_count -= 1
                num_int += 1
                part_2 = num_int.__str__()
                add_back_zeroes = 0
                #Add back any leading zeroes
                while add_back_zeroes < zeroes_count:
                    part_1 = part_1 + '0'
                    add_back_zeroes += 1
                return part_1 + part_2

            #Case 2b: We don't have a consumable zero
            else:
                num_int += 1
                part_2 = num_int.__str__()
                return part_1 + part_2




increment_string("benjamin00000999888")
