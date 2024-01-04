import logging
def setup_logging(level):
        logging.basicConfig(level=level)
import sys
def add_to_python_path(path):
        sys.path.append(path)