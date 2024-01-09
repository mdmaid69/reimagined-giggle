import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
def calculate_roi(gain, cost):
        return (gain - cost) / cost