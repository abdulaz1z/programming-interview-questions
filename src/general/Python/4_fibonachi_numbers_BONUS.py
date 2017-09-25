"""
4. Write fibonacci iteratively and recursively (bonus: use dynamic programming)

This can be further optimized by applying the following logic:
    - When checking if the number was already found and the answer is no, check 
    for previous numbers that were already answered. That way we would be 
    looping back untill we find a number that was calculated. This will save 
    computational time in the long run if we log every number that was 
    calculated on every step. Essentially we would only have to calculate 
    the numbers only once. After that we would find them in the dictionary 
    and use those to calculate the non-calculated fibonacci number that is 
    being requested to calculate. 
    
"""

"""
========== BONUS ==========
Dynamic programming: https://en.wikipedia.org/wiki/Dynamic_programming

TL/DR: Break down the problem into simpler sub-problems (divide and conquer)
and store their results for future use.

I am using dictionaries to keep track of the results that were already calculated.
"""
iterative_fib_numbers = dict()
recursive_fib_numbers = dict()

"""========================"""

# Fibonachi recursively (function calls itself)
def fib(nth_number):
    """Returns the nth fibonacci number recursively and stores it's result for future use."""

    print("\nCalculating "+nth_number.__str__()+" recursively...")

    # check if we already calculated the nth fib number and return it if we saved it
    if nth_number in recursive_fib_numbers:
        print("fib number "+nth_number.__str__()+" found in cache")
        print("Recursive cahce: " + recursive_fib_numbers.__str__())
        return recursive_fib_numbers[nth_number]

    if nth_number == 0:
        return 0
    elif nth_number == 1:
        return 1
    else:
        iter_answer = fib(nth_number-1) + fib(nth_number - 2)
        recursive_fib_numbers[nth_number] = iter_answer
        return iter_answer


# Fibonachi iteratively (use a loop)
def fib_iter(nth_number):
    """Returns the nth fibonacci number iteratively and stores it's result for future use."""

    print("\nCalculating "+nth_number.__str__()+" iteratively...")

    if nth_number in iterative_fib_numbers:
        print("fib number "+nth_number.__str__()+" found in cache")
        print("Iterative cache: " + iterative_fib_numbers.__str__())
        return iterative_fib_numbers[nth_number]

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
            iterative_fib_numbers[x] = result

            # update the previous 2 numbers
            prev_previous = prev
            prev = result
        return result

if __name__ == '__main__':
    """ create a list of the first 10 fibonacci numbers and store them in a list"""
    print("Generating the first 10 fibonacci numbers iteratively and recursively")
    fib_numbers = [fib(x) for x in range(1, 11)]
    fib_iter_numbers = [fib_iter(x) for x in range(1, 11)]
    print("Recursive list of fibonacci numbers: "+str(fib_numbers))
    print("Iterative list of fibonacci numbers: "+str(fib_iter_numbers))
    print("="*40)
    print("calculating numbers a second time through \n")
    print("Recursive cache: "+recursive_fib_numbers.__str__())
    print("Iterative cache: "+iterative_fib_numbers.__str__())
    fib_numbers2 = [fib(x) for x in range(1, 11)]
    fib_iter_numbers2 = [fib_iter(x) for x in range(1, 11)]
    print("Recursive list of fibonacci numbers: "+str(fib_numbers2))
    print("Iterative list of fibonacci numbers: "+str(fib_iter_numbers2))



