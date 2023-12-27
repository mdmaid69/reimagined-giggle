n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b
import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")