import os
def get_environment_variable(var):
        return os.getenv(var)
import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")