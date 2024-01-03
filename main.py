import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
n = 10
print("Cube numbers:", [x**3 for x in range(n)])