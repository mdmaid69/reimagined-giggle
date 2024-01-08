import sys
def add_to_python_path(path):
        sys.path.append(path)
def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps