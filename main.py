import tensorflow as tf
print(tf.__version__)
def calculate_roi(gain, cost):
        return (gain - cost) / cost