import logging
def setup_logging(level):
        logging.basicConfig(level=level)
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)