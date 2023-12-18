import getpass
def get_username():
        return getpass.getuser()
import json
print(json.dumps({"name": "John", "age": 30}))