n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)
import logging
def setup_logging(level):
        logging.basicConfig(level=level)