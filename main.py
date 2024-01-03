import shutil
def delete_directory(path):
        shutil.rmtree(path)
def calculate_volume(length, width, height):
        return length * width * height