  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)
import sklearn.datasets
print(sklearn.datasets.load_iris())