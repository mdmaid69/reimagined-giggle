def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal
import shutil
def move_file(src, dst):
        shutil.move(src, dst)