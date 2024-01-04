  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"
import sklearn.datasets
print(sklearn.datasets.load_iris())