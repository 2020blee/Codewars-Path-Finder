import math

color1 = " "
color2 = " "
color3 = " "

#The idea here is for the function to take in a variable like color1 as well as an integer and set the variable depending on the integer being taken in. However, it doesn't work
def num_color_code(int, var):
    if int == 0:
        var = "black"
    elif int == 1:
        var = "brown"
    elif int == 2:
        var = "red"
    elif int == 3:
        var = "orange"
    elif int == 4:
        var = "yellow"
    elif int == 5:
        var = "green"
    elif int == 6:
        var = "blue"
    elif int == 7:
        var = "violet"
    elif int == 8:
        var = "gray"
    else:
        var = "white"


def encode_resistor_colors(ohms_string):
    #print(ohms_string[0])
    #print(len(ohms_string))

    #Checks where the space is in the string because the space and the ohms is unnecssary information
    #I put a count because the string only needs to be sliced once (where the space is). The for loop will stop after the string is sliced once. If the for loop continues to run through the string after the slice, errors will pop up
    count = 0
    for n in range(len(ohms_string)):
        #The slice of the string won't be happen if a slice of the string already occured.
        if count == 0:
            if ohms_string[n] == " ":
                new_string = ohms_string[:n]
                count += 1
    #Now we just have the number to work with in new_string

    #I need to know if the string ends in k or M. These two statements will figure it out

    if new_string[len(new_string)-1] == "k":
        #This lops off the k off the string, so we just have a float
        new_string = new_string[:len(new_string)-1]
        num = float(new_string) * 1000
        float_length = math.floor(math.log10(num)) + 1
        num_color_code(float_length, color3)
        #Lops off everything except the first two digits
        num = math.floor(num / 10^{float_length})
        final_string = str(num)
        #The first two numbers in the string correspond to the first and second colors
        num_color_code(final_string[0], color1)
        num_color_code(final_string[1], color2)
        #Putting everything together
        return(color1 + " " + color2 + " " + color3 + " " + "gold")

    elif new_string[len(new_string)-1] == "M":
        #This lops off the M off the string, so we just have a float
        new_string = new_string[:len(new_string)-1]
        num = float(new_string) * 1000000
        float_length = math.floor(math.log10(num)) + 1
        num_color_code(float_length, color3)
        #Lops off everything except the first two digits
        num = math.floor(num / 10^{float_length})
        final_string = str(num)
        #The first two numbers in the string correspond to the first and second colors
        num_color_code(final_string[0], color1)
        num_color_code(final_string[1], color2)
        #Putting everything together
        return(color1 + " " + color2 + " " + color3 + " " + "gold")

    else:
        num = float(new_string)
        float_length = math.floor(math.log10(num)) + 1
        num_color_code(float_length, color3)
        final_string = str(num)
        #The first two numbers in the string correspond to the first and second colors
        num_color_code(final_string[0], color1)
        num_color_code(final_string[1], color2)
        #Putting everything together
        return(color1 + " " + color2 + " " + color3 + " " + "gold")
