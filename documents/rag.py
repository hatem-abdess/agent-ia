import os
import chromadb
from pypdf import PdfReader
from docx import Document
from llm import demander_llm


def lire_document(chemin):
    if chemin.endswith(".txt"):
        with open(chemin, "r", encoding="utf-8") as f:
            return f.read()
    if chemin.endswith(".pdf"):
        lecteur = PdfReader(chemin)
        return "\n".join(page.extract_text() or "" for page in lecteur.pages)
    if chemin.endswith(".docx"):
        doc = Document(chemin)
        return "\n".join(p.text for p in doc.paragraphs)
    return ""


def decouper(texte, taille=300):
    morceaux = []
    for i in range(0, len(texte), taille):
        morceaux.append(texte[i:i + taille])
    return morceaux


client = chromadb.Client()
collection = client.get_or_create_collection("documents")

for nom in os.listdir("documents"):
    texte = lire_document(os.path.join("documents", nom))
    for i, morceau in enumerate(decouper(texte)):
        collection.add(ids=[f"{nom}-{i}"], documents=[morceau], metadatas=[{"source": nom}])

print("Morceaux indexés :", collection.count())


def rechercher(question, n=2):
    resultats = collection.query(query_texts=[question], n_results=n)
    return resultats["documents"][0]


def repondre(question):
    contexte = "\n".join(rechercher(question))
    prompt = f"""Tu es l'assistant RH de l'entreprise. Réponds en français, en 2 phrases maximum,
uniquement à partir du contexte ci-dessous. Si la réponse n'y est pas, dis "Je ne sais pas".

Contexte :
{contexte}

Question : {question}"""
    return demander_llm(prompt)


if __name__ == "__main__":
    while True:
        question = input("Vous : ")
        if question.lower() == "quit":
            break
        print("Assistant :", repondre(question))
