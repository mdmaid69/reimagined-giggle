import tensorflow as tf
print(tf.__version__)
import math
def calculate_complementary_error_function(x):
        return math.erfc(x)