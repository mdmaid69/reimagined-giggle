  import datetime
  def get_current_date():
        return datetime.datetime.now().date()
import json
print(json.dumps({"name": "John", "age": 30}))