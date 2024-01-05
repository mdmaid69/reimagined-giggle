import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
n = 10
print("Even numbers:", [x for x in range(n) if x % 2 == 0])