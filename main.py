  import datetime
  def get_current_date():
        return datetime.datetime.now().date()
sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))