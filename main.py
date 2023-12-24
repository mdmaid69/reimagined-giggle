import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
def calculate_pressure(force, area):
        return force / area