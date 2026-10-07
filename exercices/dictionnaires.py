employe = {
    "nom": "Sami",
    "poste": "Technicien",
    "conges": 30,
}

print(employe["nom"])
print(employe.get("salaire", "non renseigné"))

employe["service"] = "Maintenance"
print(employe)

for cle, valeur in employe.items():
    print(cle, "→", valeur)