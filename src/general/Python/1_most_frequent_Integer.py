"""
1-Find the most frequent integer in an array
"""

def most_frequent_integer(array):
    #a dictionary to map out the unique values and its frequencies
    frequencies = dict()

    for i in array:
        if i not in frequencies:
            frequencies[i] = 1
        else:
            frequencies[i] += 1

    k = ""      #keeps track of the most frequent key
    v = -1      #keeps track of the highest value(frequency)

    for key, value in frequencies.items(): #iterates throught the dict using tuples
        if value > v:
            k = key
            v = value
#    print(k, ' is the most frequent integer with ', v, ' instances')
    return k


if __name__ == '__main__':
    test_array = "3456789865431213232"
    answer = most_frequent_integer(test_array) #answer should be 3 is the most frequent with 4 instances
    print('the most frequent integer is ', answer)
