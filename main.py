import getpass
def get_username():
        return getpass.getuser()
def is_palindrome(s):
        return s == s[::-1]