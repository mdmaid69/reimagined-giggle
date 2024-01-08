import tensorflow as tf
print(tf.__version__)
def calculate_profit_margin(revenue, cost):
        return (revenue - cost) / revenue