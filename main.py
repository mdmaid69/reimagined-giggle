def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))
import shutil
def move_file(src, dst):
        shutil.move(src, dst)