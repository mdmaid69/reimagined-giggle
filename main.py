import os
def get_file_size(filename):
        return os.path.getsize(filename)
def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps