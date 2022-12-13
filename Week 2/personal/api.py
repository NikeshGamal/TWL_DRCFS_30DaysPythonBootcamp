import requests

#request--->synchronous
response = requests.get("https://my-json-server.typicode.com/typicode/demo/posts")

# response = requests.get("https://www.google.com/")

print(response.json())