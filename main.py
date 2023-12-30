import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")