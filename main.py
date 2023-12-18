import os
def remove_directory(path):
        os.rmdir(path)
def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps