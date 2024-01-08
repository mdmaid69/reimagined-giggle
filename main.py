import shutil
def delete_directory(path):
        shutil.rmtree(path)
def calculate_current_ratio(current_assets, current_liabilities):
        return current_assets / current_liabilities