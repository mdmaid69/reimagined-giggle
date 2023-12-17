  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)
text = "Hello, world!"
print("Words:", len(text.split()))