def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)
import shutil
def move_file(src, dst):
        shutil.move(src, dst)