def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)
import sklearn.datasets
print(sklearn.datasets.load_iris())