import os
def get_environment_variable(var):
        return os.getenv(var)
import json
print(json.dumps({"name": "John", "age": 30}))