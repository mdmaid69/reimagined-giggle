import platform
def get_os_info():
        return platform.uname()
def calculate_energy(mass, c=3*10**8):
        return mass * c**2