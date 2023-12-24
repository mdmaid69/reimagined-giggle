import tensorflow as tf
print(tf.__version__)
def calculate_average(numbers):
        return sum(numbers) / len(numbers)