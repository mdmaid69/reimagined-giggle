  import datetime
  def get_current_date():
        return datetime.datetime.now().date()
def find_unique_words(sentence):
        return set(sentence.split())