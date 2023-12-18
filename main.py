import tensorflow as tf
print(tf.__version__)
def calculate_eps(net_income, shares_outstanding):
        return net_income / shares_outstanding