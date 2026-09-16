
import requests

# Jsonplaceholder api
url_placeholder = "https://jsonplaceholder.typicode.com/posts"

# Query parameter
data ={
    "Title": "Professional Programmer",
    "body": "Some text about my experience",
    "userId": 1
}

response_placeholder = requests.post(url_placeholder, data=data)
print(response_placeholder.text)