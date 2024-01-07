import tensorflow as tf
print(tf.__version__)
n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))