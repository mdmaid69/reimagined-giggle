import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)
def calculate_roi(gain, cost):
        return (gain - cost) / cost