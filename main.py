import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")