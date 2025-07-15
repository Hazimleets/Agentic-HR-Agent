import requests

url = "http://127.0.0.1:5000/rag_generate"
query = {"prompt": "What is the onboarding process?"}

response = requests.post(url, json=query)
print(response.json())
