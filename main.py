import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
def calculate_average(numbers):
        return sum(numbers) / len(numbers)