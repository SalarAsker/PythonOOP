# File: query_param.py

import requests

# Jsonplaceholder api
url = "https://www.bohuslaningen.se/asikt/ledare/nu-har-liberalerna-en-chans-att-utnyttja-sin-vagmastarposition.cda435b9-e785-4893-9eb4-d7da0c50afb3"

response = requests.get(url)

if response.status_code == requests.codes.ok:
    print(response.text)

# # Query parameter
# parameters ={
#     "id": 50
# }

# response_placeholder = requests.get(url_placeholder, params=parameters)

# if response_placeholder.status_code == requests.codes.ok:
#     print("Request successful")
#     print(response_placeholder.headers)
# else:
#     print("Request failed")

