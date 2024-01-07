import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps