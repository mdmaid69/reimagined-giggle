  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)
numbers = [1, 2, 3, 4, 5]
print("Average:", sum(numbers) / len(numbers))