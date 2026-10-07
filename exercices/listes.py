documents = ["rh.txt", "procedure.pdf", "formation.docx"]

print(documents[0])
print(documents[-1])
print(len(documents))

documents.append("contrat.txt")
print(documents)

for doc in documents: print("Lecture du fichier :", doc)