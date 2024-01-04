import tensorflow as tf
print(tf.__version__)
def calculate_current_ratio(current_assets, current_liabilities):
        return current_assets / current_liabilities