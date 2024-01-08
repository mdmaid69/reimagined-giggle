import tensorflow as tf
print(tf.__version__)
def count_words(sentence):
        return len(sentence.split())