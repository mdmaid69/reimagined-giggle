def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal
import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)