import requests

# Jsonplaceholder api
url_placeholder = "https://randomuser.me/api/"

# Query parameter
parameters ={
    "gender": "male",
    "results": 4
}

response_placeholder = requests.get(url_placeholder, params=parameters)

print(response_placeholder.text)

