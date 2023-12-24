import tensorflow as tf
print(tf.__version__)
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"