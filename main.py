def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps
import shutil
def delete_directory(path):
        shutil.rmtree(path)