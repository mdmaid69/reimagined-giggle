import platform
def get_python_version():
        return platform.python_version()
def calculate_energy(mass, c=3*10**8):
        return mass * c**2