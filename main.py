import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))
import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")