import tensorflow as tf
print(tf.__version__)
sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))