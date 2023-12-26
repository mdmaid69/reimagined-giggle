import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
n = 10
print("Fibonacci:", [((1 + 5**0.5) / 2)**n / 5**0.5 for n in range(n)])