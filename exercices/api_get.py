import requests

url = "https://jsonplaceholder.typicode.com/todos/1"
reponse = requests.get(url)

print(reponse.status_code)

donnees = reponse.json()
print(donnees)
print(donnees["title"])