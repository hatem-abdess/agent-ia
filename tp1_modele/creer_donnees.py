import numpy as np
import pandas as pd

rng = np.random.default_rng(42)
n = 200

anciennete = rng.integers(1, 61, n)
nb_achats = rng.integers(1, 31, n)
montant_moyen = rng.normal(150, 50, n).round(1)
reclamations = rng.integers(0, 6, n)

score = reclamations * 0.8 - nb_achats * 0.1 - anciennete * 0.03 + rng.normal(0, 0.6, n)
a_quitte = (score > 0).astype(int)

clients = pd.DataFrame({
    "anciennete_mois": anciennete,
    "nb_achats": nb_achats,
    "montant_moyen": montant_moyen,
    "reclamations": reclamations,
    "a_quitte": a_quitte,
})

clients.loc[[5, 17, 42, 88, 150], "montant_moyen"] = np.nan
clients = pd.concat([clients, clients.iloc[[0, 1, 2]]], ignore_index=True)

clients.to_csv("clients.csv", index=False)
print("Fichier clients.csv créé :", len(clients), "lignes")
