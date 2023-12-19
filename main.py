import logging
def log_message(message):
        logging.info(message)
def is_palindrome(s):
        return s == s[::-1]