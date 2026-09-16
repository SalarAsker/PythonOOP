# File: query_param.py

import requests

# Jsonplaceholder api
url_placeholder = "https://jsonplaceholder.typicode.com/posts"

# Query parameter
parameters ={
    "id": 50
}

response_placeholder = requests.get(url_placeholder, params=parameters)

if response_placeholder.status_code == requests.codes.ok:
    print("Request successful")
    print(response_placeholder.headers)
else:
    print("Request failed")

