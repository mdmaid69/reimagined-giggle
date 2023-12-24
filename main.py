import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
def calculate_debt_ratio(total_debt, total_assets):
        return total_debt / total_assets