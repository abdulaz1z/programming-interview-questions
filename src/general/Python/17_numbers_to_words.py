"""
Numbers to words.py
Author: Raymond Perez (github.com/Raymond-P)
Description: given a number write it out in words. Only supports natural numbers (positive ints).

Logic:
Our number system in english has a few general rules* when it comes to naming a number.
1- unique names:
    -numbers 0-19
    -decimals: 20,30,40,50,60,70,80 and 90
    
2- zero '0' is silent:
    -not mentioned, unless it's by itself
    
3- hundreds are almost the same as units:
    -a number in the hundred category is the name of the unit plus 'hundred'. ex: 900 nine hundred
    
4- group numbers in 3 digit groups:
    -the previous rules apply to numbers inside groups of 3 digits
    -we classify these 3 digit groups with the power of 10 associated with the rightmost (lowest) digit
    -these powers of 10 have unique names: none, thousand, million, billion, trillion, quadrillion
    -we name them using the previous rules and it's respective power of 10
     
*these rules could get more technical but these are good enough for our purposes
"""
from math import ceil

units = {
    0: "",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen"
}
decimals = {
    0: "",
    2: "twenty",
    3: "thirty",
    4: "forty",
    5: "fifty",
    6: "sixty",
    7: "seventy",
    8: "eighty",
    9: "ninety"
}

group_of_3_lvl = {
    1: "",  # 0-999
    2: "thousand ",  # 1000-9999
    3: "million ",
    4: "trillion ",
    5: "quadrillion ",
    6: "quintillion ",
    7: "sextillion ",
    8: "septillion "

}


def eval_group_of_3(group):  # a number group of 3 ex: "123"
    output = ""
    if group[0] > "0":
        output += units[int(group[0])] + " hundred "
    if group[1:] < "20":  # less than 20
        output += units[int(group[1:])]
        return output
    else:
        output += decimals[int(group[1])]+" "
        output += units[int(group[2])]
        return output


def translate_number(number):
    if len(str(number)) > 24:                    # check if the number is supported
        return "ERROR Number too big to translate for now."
    if number == 0:                              # unique case 'zero'
        return "zero"
    input_str = str(number)                      # parse number to string because we will use te string indexing feature
    padding = ""                                 # we add padding to a sure the len of input_str is a multiple of 3
    for i in range(3 - (len(input_str)%3)):
        padding += "0"
    input_str = padding + input_str
    num_of_groups = ceil(len(input_str)/3)       # we calculate how many groups of 3 digits are in the number that way
    output = ""                                  # ^we know what level:"thousand", "million" the groups classify in
    while num_of_groups > 0:                     # ^and use this number as a key in our group_of_3_lvl dict
        current_translation = eval_group_of_3(input_str[0:3])
        if len(current_translation) != 0:
            current_translation += " " + group_of_3_lvl[num_of_groups]
        output = output + current_translation
        num_of_groups -= 1
        input_str = input_str[3:]
    return output


if __name__ == '__main__':
    print(translate_number(122347273013120000000000))
    print(translate_number(000))