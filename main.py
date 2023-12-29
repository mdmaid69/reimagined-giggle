import os
def change_working_directory(path):
        os.chdir(path)
def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps