  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)
import logging
def setup_logging(level):
        logging.basicConfig(level=level)