import json
print(json.dumps({"name": "John", "age": 30}))
import getpass
def get_password(prompt):
        return getpass.getpass(prompt)