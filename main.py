import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
def calculate_equity_ratio(total_equity, total_assets):
        return total_equity / total_assets