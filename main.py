def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
import sklearn.datasets
print(sklearn.datasets.load_iris())