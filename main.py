import shutil
def delete_directory(path):
        shutil.rmtree(path)
def calculate_pressure(force, area):
        return force / area