import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)
def is_palindrome(s):
        return s == s[::-1]