import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
def calculate_return_on_assets(net_income, total_assets):
        return net_income / total_assets