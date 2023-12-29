import logging
def setup_logging(level):
        logging.basicConfig(level=level)
import os
def get_environment_variable(var):
        return os.getenv(var)