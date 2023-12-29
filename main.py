import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)
def calculate_energy(mass, c=3*10**8):
        return mass * c**2