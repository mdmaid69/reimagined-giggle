import shutil
def delete_directory(path):
        shutil.rmtree(path)
def calculate_work(force, distance):
        return force * distance