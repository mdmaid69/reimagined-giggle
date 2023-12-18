def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)
import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")