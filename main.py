import tensorflow as tf
print(tf.__version__)
def is_palindrome(s):
        return s == s[::-1]