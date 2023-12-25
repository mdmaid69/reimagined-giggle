import shutil
def move_file(src, dst):
        shutil.move(src, dst)
def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps