import tensorflow as tf
print(tf.__version__)
def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time