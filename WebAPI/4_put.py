import requests

# targeting post with id 5, according to the documentation
url =  "https://jsonplaceholder.typicode.com/posts/5"

# change title and data
data = {
    "title" : "New Title",
    "body" : "The post has been updated",
    "id" : 5,
    "userId": 1
}
response = requests.put(url, data=data)
print(response.text)


