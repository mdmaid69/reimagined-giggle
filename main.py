def calculate_roi(gain, cost):
        return (gain - cost) / cost
import shutil
def delete_directory(path):
        shutil.rmtree(path)