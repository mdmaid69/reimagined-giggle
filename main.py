import getpass
def get_password(prompt):
        return getpass.getpass(prompt)
def calculate_energy(mass, c=3*10**8):
        return mass * c**2