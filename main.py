import shutil
def move_file(src, dst):
        shutil.move(src, dst)
def is_palindrome(s):
        return s == s[::-1]