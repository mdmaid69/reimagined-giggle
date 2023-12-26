def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities
import tensorflow as tf
print(tf.__version__)