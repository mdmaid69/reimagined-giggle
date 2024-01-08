import sklearn.datasets
print(sklearn.datasets.load_iris())
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())