import shutil
def delete_directory(path):
        shutil.rmtree(path)
def calculate_debt_ratio(total_debt, total_assets):
        return total_debt / total_assets