import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
def calculate_current_ratio(current_assets, current_liabilities):
        return current_assets / current_liabilities