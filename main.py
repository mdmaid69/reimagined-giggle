import tensorflow as tf
print(tf.__version__)
def calculate_energy(mass, c=3*10**8):
        return mass * c**2