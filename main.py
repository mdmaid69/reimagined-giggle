import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
def calculate_debt_ratio(total_debt, total_assets):
        return total_debt / total_assets