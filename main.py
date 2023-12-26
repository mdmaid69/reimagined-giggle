def calculate_profit_margin(revenue, cost):
        return (revenue - cost) / revenue
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)