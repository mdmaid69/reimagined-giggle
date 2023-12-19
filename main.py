  import datetime
  def get_current_date():
        return datetime.datetime.now().date()
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))