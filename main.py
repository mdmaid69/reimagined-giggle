import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
def calculate_force(mass, acceleration):
        return mass * acceleration