import requests

url = "https://jsonplaceholder.typicode.com/posts/99"

response = requests.delete(url)

print(response.text)