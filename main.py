def is_palindrome(s):
        return s == s[::-1]
import shutil
def delete_directory(path):
        shutil.rmtree(path)