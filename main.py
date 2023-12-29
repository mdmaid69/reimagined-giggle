import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
import sys
def add_to_python_path(path):
        sys.path.append(path)