def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)
import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)