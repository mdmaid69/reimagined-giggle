def is_palindrome(s):
        return s == s[::-1]
import logging
def setup_logging(level):
        logging.basicConfig(level=level)