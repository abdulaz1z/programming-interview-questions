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
        -we usually see this as the commas that separate the number in groups of 3
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

# Think of this dictionary as the commas in a number.
# ex: 500,200,200
# five hundred ('million') two hundred ('thousand') two hundred ('')
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


def eval_group_of_3(number_str):  # a number group of 3 ex: "123"
    """
    translates a 3 digit number to words
    :param number_str: the string of the number to evaluate. ex: "123"
    :return: a string with the verbal representation of the number. 
        ex: "123" -> "one hundred twenty three"
    """
    output = ""
    if number_str[0] > "0":
        output += units[int(number_str[0])] + " hundred "
    if number_str[1:] < "20":  # check if decimal less than 20 ex: 312 -> 12 < 20? true
        output += units[int(number_str[1:])]  # look for the decimal in the units dictionary
        return output  # we evaluated all 3 digits
    else:
        output += decimals[int(number_str[1])] + " "  # get the decimal name
        output += units[int(number_str[2])]           # get the unit name
        return output


def add_padding(string):
    """
    Adds padding to the string as 0's to ensure that the 
    length of the string is a multiple of 3
    :param string: the number string to be padded
    ex: 12,345 -> 012,345
    """
    padding = ""
    for i in range(3 - (len(string) % 3)):
        padding += "0"
    return padding + string


def translate_number(number):
    # parse number to string because we will use the string indexing feature
    input_str = str(number)
    if not input_str.isnumeric():         # check if it is a number
        return "Input Error: argument passed in is not a number"
    if len(str(number)) > 24:             # check if the number is supported
        return "ERROR Number too big to translate for now."
    if number == 0:                       # unique case 'zero'
        return "zero"


    input_str = add_padding(input_str)  # add padding to the string

    # we evaluate numbers in groups of 3 therefore find out
    # how many groups of 3 there are
    num_of_groups = ceil(len(input_str)/3)  # we also use this to keep track of the group lvl

    output = ""  # keep track of the string we are going to return
    while num_of_groups > 0:
        # keep track of what the current group of 3 translates to
        current_translation = eval_group_of_3(input_str[0:3])

        # make sure we don't add a lvl to an empty translation
        # ex: 30,000,000 -> thirty million
        # not thirty million thousand
        if len(current_translation) != 0:
            current_translation += " " + group_of_3_lvl[num_of_groups]

        output = output + current_translation  # add current translation to output
        num_of_groups -= 1  # decrement the group level
        input_str = input_str[3:]  # delete the first group of 3 from the number string
    return output


if __name__ == '__main__':
    print(translate_number(122347273013120000000000))
    print(translate_number(000))