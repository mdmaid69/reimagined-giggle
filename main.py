def calculate_energy(mass, c=3*10**8):
        return mass * c**2
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)