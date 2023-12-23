import sklearn.datasets
print(sklearn.datasets.load_iris())
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b