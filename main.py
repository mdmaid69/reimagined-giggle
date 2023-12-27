import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
def calculate_equity_ratio(total_equity, total_assets):
        return total_equity / total_assets