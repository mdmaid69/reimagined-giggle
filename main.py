import shutil
def delete_directory(path):
        shutil.rmtree(path)
def calculate_perimeter_rectangle(l, w):
        return 2 * (l + w)