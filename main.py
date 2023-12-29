import shutil
def move_file(src, dst):
        shutil.move(src, dst)
def calculate_energy(mass, c=3*10**8):
        return mass * c**2