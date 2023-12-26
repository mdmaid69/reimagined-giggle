import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
def is_prime(n):
        for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                return False
        return True