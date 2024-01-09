import tensorflow as tf
print(tf.__version__)
n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])