import os
def list_files_in_directory(path):
        return os.listdir(path)
def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))