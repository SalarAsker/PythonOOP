import requests


url = "https://httpbin.org/get"

headers = {
    "Accept": "application/json"
}

params = {
    "department": "computer-science"
}
try:
   response = requests.get(url,params=params,headers=headers)
   response.raise_for_status()
except requests.exceptions.HTTPError as error:
    print(f"HTTP error:{error}")

if response.status_code == requests.codes.ok:
    print("URL:", response.url)
    print("Status:", response.status_code)
    print("Content-Type:", response.headers["Content-Type"])
    print("Text", response.text)
  

