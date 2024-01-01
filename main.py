import shutil
def delete_directory(path):
        shutil.rmtree(path)
def calculate_force(mass, acceleration):
        return mass * acceleration