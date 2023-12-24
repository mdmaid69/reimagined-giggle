import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps