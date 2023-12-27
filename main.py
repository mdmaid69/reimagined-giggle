import sys
def add_to_python_path(path):
        sys.path.append(path)
def calculate_energy(mass, c=3*10**8):
        return mass * c**2