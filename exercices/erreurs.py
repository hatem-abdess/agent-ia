import requests

try:
    reponse = requests.get("http://localhost:11434", timeout=5)
    print("Ollama répond :", reponse.text)
except requests.exceptions.ConnectionError:
    print("Erreur : Ollama n'est pas démarré.")