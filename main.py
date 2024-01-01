import tensorflow as tf
print(tf.__version__)
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())