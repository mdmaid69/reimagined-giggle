import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
n = 10
print("Powers of 2:", [2**x for x in range(n)])