import tensorflow as tf
print(tf.__version__)
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time