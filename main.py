import itertools
print(list(itertools.permutations([1, 2, 3])))
def is_palindrome(s):
        return s == s[::-1]