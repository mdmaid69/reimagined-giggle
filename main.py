import sys
def print_python_version():
        print(sys.version)
import logging
def setup_logging(level):
        logging.basicConfig(level=level)