"""
4. Write fibonacci iteratively and recursively (bonus: use dynamic programming)
"""

# Fibonachi recursively (function calls itself)
def fib(nth_number):
    if nth_number == 0:
        return 0
    elif nth_number == 1:
        return 1
    else:
        return fib(nth_number-1) + fib(nth_number - 2)


# Fibonachi iteratively (use a loop)
def fib_iter(nth_number):
    if nth_number == 0:
        return 0
    if nth_number == 1:
        return 1
    else:
        """
        we have to keep track of the previous 2 numbers 
        (assuming we are in the 2nd fibonacci number)
        """
        prev_previous = 0
        prev = 1
        result = 0
        for x in range(2, nth_number+1): # range stop parameter is non-inclusive
            result = prev_previous + prev

            # update the previous 2 numbers
            prev_previous = prev
            prev = result
        return result

if __name__ == '__main__':
    """ create a list of the first 10 fibonacci numbers and store them in a list"""
    print("Generating the first 10 fibonacci numbers iteratively and recursively")
    fib_numbers = [fib(x) for x in range(1, 11)]
    fib_iter_numbers = [fib_iter(x) for x in range(1,11)]
    print("Recursive list of fibonacci numbers: "+str(fib_numbers))
    print("Iterative list of fibonacci numbers: "+str(fib_iter_numbers))



