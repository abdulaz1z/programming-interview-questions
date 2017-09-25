"""
5.Check if a String is composed of all unique characters

"""

def contains_unique_chars(self):
    unique_chars = []
    for char in self:
        if char in unique_chars:
            return False
        else:
            unique_chars.append(char)
    return True

if __name__ == '__main__':
    test1 = "123"
    print("is test1 ("+test1+") composed only of unique characters? ")
    print(contains_unique_chars(test1))
    print("="*20)
    test2 = "122"
    print("is test2 ("+test2+") composed only of unique characters? ")
    print(contains_unique_chars(test2))