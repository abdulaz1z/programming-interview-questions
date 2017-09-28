"""
Numbers to words.py
Description: given a number write it out in words

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
    4: "fourty",
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
    input_str = str(number)
    padding = ""
    for i in range(3 - (len(input_str)%3)):
        padding += "0"
    input_str = padding + input_str
    num_of_groups = ceil(len(input_str)/3)
    output = ""
    while num_of_groups > 0:
        current_translation = eval_group_of_3(input_str[0:3])
        if len(current_translation) != 0:
            current_translation += " " + group_of_3_lvl[num_of_groups]
        output = output + current_translation
        num_of_groups -= 1
        input_str = input_str[3:]
    return output


if __name__ == '__main__':
    print(eval_group_of_3("123"))
    # print(eval_group_of_3("000"))
    # print(eval_group_of_3("23")) # fix bug
    print(translate_number(122347273000000))