def calculate_roi(gain, cost):
        return (gain - cost) / cost
import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()