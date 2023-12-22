import sklearn.datasets
print(sklearn.datasets.load_iris())
list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Common elements:", set(list1) & set(list2))