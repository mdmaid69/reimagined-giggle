import tensorflow as tf
print(tf.__version__)
def find_unique_words(sentence):
        return set(sentence.split())