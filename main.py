  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)
import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")