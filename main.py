import tensorflow as tf
print(tf.__version__)
def calculate_interest(principal, rate, time):
        return principal * (1 + rate)**time