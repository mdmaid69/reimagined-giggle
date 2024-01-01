def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal
import sklearn.datasets
print(sklearn.datasets.load_iris())