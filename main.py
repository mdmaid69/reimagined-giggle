import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
def is_palindrome(s):
        return s == s[::-1]