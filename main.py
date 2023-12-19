import logging
def setup_logging(level):
        logging.basicConfig(level=level)
  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value