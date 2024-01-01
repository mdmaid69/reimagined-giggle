import tensorflow as tf
print(tf.__version__)
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)