n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)
  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)