import shutil
def delete_directory(path):
        shutil.rmtree(path)
def calculate_density(mass, volume):
        return mass / volume