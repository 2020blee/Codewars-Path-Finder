def encrypt(text, encryptKey):
    region_1a = list("qwertyuiop")
    region_1b = list("QWERTYUIOP")
    region_2a = list("asdfghjkl")
    region_2b = list("ASDFGHJKL")
    region_3a = list("zxcvbnm,.")
    region_3b = list("ZXCVBNM<>")
    encryptKey = list(str(encryptKey))
    new_encryptKey = []
    #encryptKey is a string, but we should turn it into an array to make it easier to bookkeep the shift values
    for i in encryptKey:
        k = int(i)
        new_encryptKey.append(k)
    #The 0s are just there as placeholders. They are placed at the beginning so 6 becomes 006
    if len(new_encryptKey) == 2:
        new_encryptKey.append(0)
    if len(new_encryptKey) == 1:
        new_encryptKey.append(0)
        new_encryptKey.append(0)
    output = []
    text = list(text)
    #This filters out any symbols that aren't in the regions like 6 or $
    for n in region_1a or region_2a or region_3a or region_1b or region_2b or region_3b:
        #Looks at every character individually in the text
        for l in text:
            #Checks which region the character is in
            if l in region_1a:
                #Takes the index of that character within its region and shifts it based on the encryptKey
                val = (region_1a.index(l) + new_encryptKey[0]) % 10
                #The shifted character is added to the array for the output
                output.append(region_1a[val])
            elif l in region_1b:
                val = (region_1b.index(l) + new_encryptKey[0]) % 10
                output.append(region_1b[val])
            elif l in region_2a:
                val = (region_2a.index(l) + new_encryptKey[1]) % 9
                output.append(region_2a[val])
            elif l in region_2b:
                val = (region_2b.index(l) + new_encryptKey[1]) % 9
                output.append(region_2b[val])
            elif l in region_3a:
                val = (region_3a.index(l) + new_encryptKey[2]) % 9
                output.append(region_3a[val])
            elif l in region_3b:
                val = (region_3b.index(l) + new_encryptKey[2]) % 9
                output.append(region_3b[val])
            elif l not in region_1a or region_2a or region_3a or region_1b or region_2b or region_3b:
                output.append(l)
            else:
                output.append(l)
        #The outputs are all joined together in a string to be returned
        return "".join(output)

#Decrypt works very similar to encrypt
def decrypt(text, encryptKey):
    region_1a = list("qwertyuiop")
    region_1b = list("QWERTYUIOP")
    region_2a = list("asdfghjkl")
    region_2b = list("ASDFGHJKL")
    region_3a = list("zxcvbnm,.")
    region_3b = list("ZXCVBNM<>")
    encryptKey = list(str(encryptKey))
    new_encryptKey = []
    #encryptKey is a string, but we should turn it into an array to make it easier to bookkeep the shift values
    for i in encryptKey:
        k = int(i)
        new_encryptKey.append(k)
    #The 0s are just there as placeholders
    if len(new_encryptKey) == 2:
        new_encryptKey.append(0)
    if len(new_encryptKey) == 1:
        new_encryptKey.append(0)
        new_encryptKey.append(0)
    output = []
    text = list(text)
    for n in region_1a or region_2a or region_3a or region_1b or region_2b or region_3b:
        for l in text:
            if l in region_1a:
                val = (region_1a.index(l) - new_encryptKey[0]) % 10
                output.append(region_1a[val])
            elif l in region_1b:
                val = (region_1b.index(l) - new_encryptKey[0]) % 10
                output.append(region_1b[val])
            elif l in region_2a:
                val = (region_2a.index(l) - new_encryptKey[1]) % 9
                output.append(region_2a[val])
            elif l in region_2b:
                val = (region_2b.index(l) - new_encryptKey[1]) % 9
                output.append(region_2b[val])
            elif l in region_3a:
                val = (region_3a.index(l) - new_encryptKey[2]) % 9
                output.append(region_3a[val])
            elif l in region_3b:
                val = (region_3b.index(l) - new_encryptKey[2]) % 9
                output.append(region_3b[val])
            elif l not in region_1a or region_2a or region_3a or region_1b or region_2b or region_3b:
                output.append(l)
        return "".join(output)
