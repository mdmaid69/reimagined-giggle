  import requests
  def get_web_page(url):
        response = requests.get(url)
        return response.text if response.status_code == 200 else "Unable to fetch web page"
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))