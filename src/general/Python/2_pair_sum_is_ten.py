"""
2- Find pairs in an integer array whose sum is equal to 10 (bonus: do it in linear time) (Done)
"""


def pairs_that_to_ten(input_array):
    array = input_array.copy()      #make a copy of the array since arrays are passed by reference in python
    pairs = []                      #array of pairs(arrays) to be returned
    while len(array)>1:
        last_int = array.pop()      #pop() takes out and returns the last element of an array

        """
        iterate over array to see if the sum of the current 
        last_int and each element in the array minus last_int
        are equal to 10
        """
        for i in array:
            if last_int + i == 10:
                pairs.append([last_int, i])

    return pairs


if __name__ == '__main__':
    my_array = [2, 3, 4, 5, 6, 7, 8,1,23,3,3,453,32,2,3,45,6,9,3]
    print(pairs_that_to_ten(my_array))
