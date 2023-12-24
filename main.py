import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
def calculate_return_on_assets(net_income, total_assets):
        return net_income / total_assets