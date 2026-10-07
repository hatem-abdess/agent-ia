import requests

URL = "http://localhost:11434/api/generate"
MODELE = "llama3.2"


def demander_llm(prompt, modele=MODELE):
    donnees = {"model": modele, "prompt": prompt, "stream": False}
    try:
        reponse = requests.post(URL, json=donnees, timeout=120)
        return reponse.json()["response"]
    except requests.exceptions.ConnectionError:
        return "Erreur : Ollama n'est pas démarré."


if __name__ == "__main__":
    print(demander_llm("Explique l'intelligence artificielle en une phrase."))
