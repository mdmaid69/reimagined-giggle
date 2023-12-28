def is_palindrome(s):
        return s == s[::-1]
import glob
def find_files(pattern):
        return glob.glob(pattern)