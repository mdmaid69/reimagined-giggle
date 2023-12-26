import sklearn.datasets
print(sklearn.datasets.load_iris())
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)