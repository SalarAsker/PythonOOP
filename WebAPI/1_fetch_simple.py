
import requests

# Random User API
url_random = "https://randomuser.me/api"
response_random = requests.get(url_random)
print(response_random.text)

# Jsonplaceholder api
url_placeholder = "https://jsonplaceholder.typicode.com/posts"
response_placeholder = requests.get(url_placeholder)
print(response_placeholder.text)

# Open meteo
url_open = """https://api.open-meteo.com/v1/forecast?latitude=59.91&longitude=10.75&hourly=temperature_2m&models=metno_seamless&forecast_days=3"""
response_open = requests.get(url_open)
print(response_open.text)