def is_palindrome(s):
        return s == s[::-1]
import getpass
def get_password(prompt):
        return getpass.getpass(prompt)