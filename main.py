import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
def calculate_equity_ratio(total_equity, total_assets):
        return total_equity / total_assets