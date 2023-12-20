import tensorflow as tf
print(tf.__version__)
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))