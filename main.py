import sklearn.datasets
print(sklearn.datasets.load_iris())
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)