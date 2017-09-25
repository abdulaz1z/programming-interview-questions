"""
4.Check if String is a palindrome
"""


def is_palindrome(self):
    if len(self) < 2: #strings of length 0 and 1 are palindromes
        return True
    else:
        if self[0] == self[len(self)-1]:
            return is_palindrome(self[1:len(self)-1])
        else:
            return False

if __name__ == '__main__':
    test1 = "racecar" #palindrome
    print("is test1 'racecar' a palindrome? ")
    print(is_palindrome(test1))

    test2 = 'hello world'
    print("is test2 'hello world' a palindrome? ")
    print(is_palindrome(test2))