import shutil
def move_file(src, dst):
        shutil.move(src, dst)
def calculate_roi(gain, cost):
        return (gain - cost) / cost