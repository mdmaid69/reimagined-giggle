import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)