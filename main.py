def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time
import sklearn.datasets
print(sklearn.datasets.load_iris())