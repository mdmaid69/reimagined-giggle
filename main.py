import tensorflow as tf
print(tf.__version__)
text = "Hello, world!"
print("Is palindrome:", text == text[::-1])