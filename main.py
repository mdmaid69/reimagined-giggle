import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()