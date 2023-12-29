import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value