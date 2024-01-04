def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal
import tensorflow as tf
print(tf.__version__)