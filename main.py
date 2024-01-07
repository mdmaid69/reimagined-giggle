def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps
import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)