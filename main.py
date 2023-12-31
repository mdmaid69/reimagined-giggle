import sklearn.datasets
print(sklearn.datasets.load_iris())
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)