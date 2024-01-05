import glob
def find_files(pattern):
        return glob.glob(pattern)
def calculate_current_ratio(current_assets, current_liabilities):
        return current_assets / current_liabilities