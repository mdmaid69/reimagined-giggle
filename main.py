import sys
def add_to_python_path(path):
        sys.path.append(path)
def calculate_roi(gain, cost):
        return (gain - cost) / cost