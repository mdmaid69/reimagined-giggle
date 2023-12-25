import os
def list_files_in_directory(path):
        return os.listdir(path)
def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps