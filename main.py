def calculate_energy(mass, c=3*10**8):
        return mass * c**2
import shutil
def delete_directory(path):
        shutil.rmtree(path)