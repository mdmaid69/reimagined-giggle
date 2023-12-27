import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
numbers = [1, 2, 3, 4, 5]
print("Squared:", [n**2 for n in numbers])