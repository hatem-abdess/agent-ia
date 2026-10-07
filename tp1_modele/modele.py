import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.metrics import accuracy_score, confusion_matrix
import joblib

# Étape 1 bis : explorer
clients = pd.read_csv("clients.csv")
print(clients.head())
print("Dimensions :", clients.shape)

print(clients.isna().sum())
print("Doublons avant le nettoyage :", clients.duplicated().sum())

clients = clients.drop_duplicates() 
mediane = clients["montant_moyen"].median() 
clients["montant_moyen"] = clients["montant_moyen"].fillna(mediane) 
print("Après nettoyage :", clients.shape) 
print("Valeurs manquantes restantes :", clients.isna().sum().sum())

print(clients.isna().sum())
print("Doublons après le nettoyage :", clients.duplicated().sum())

X = clients[["anciennete_mois", "nb_achats", "montant_moyen", "reclamations"]]
y = clients["a_quitte"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Exemples pour l'entraînement :", len(X_train))
print("Exemples pour le test :", len(X_test))

modele = DecisionTreeClassifier(max_depth=3, random_state=42)       
modele.fit(X_train, y_train)
print("Modèle entraîné !")

predictions = modele.predict(X_test)
precision = accuracy_score(y_test, predictions)
print(f"Taux de bonnes réponses : {precision:.0%}")
print("Matrice de confusion :")
print(confusion_matrix(y_test, predictions))

nouveaux_clients = pd.DataFrame({
    "anciennete_mois": [3, 48],
    "nb_achats": [2, 25],
    "montant_moyen": [90.0, 210.0],
    "reclamations": [4, 0],
})

resultats = modele.predict(nouveaux_clients)
probas = modele.predict_proba(nouveaux_clients)

for i in range(len(nouveaux_clients)):
    decision = "VA PARTIR" if resultats[i] == 1 else "reste fidèle"
    print(
        f"Client {i + 1} : {decision} "
        f"(probabilité de départ : {probas[i][1]:.0%})"
    )

joblib.dump(modele, "modele_clients.pkl")
print("Modèle sauvegardé dans modele_clients.pkl")

from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

# ...existing code...
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

foret = RandomForestClassifier(n_estimators=100, random_state=42)
foret.fit(X_train, y_train)
print(f"Random Forest : {accuracy_score(y_test, foret.predict(X_test)):.0%}")

logistique = LogisticRegression(max_iter=1000)
logistique.fit(X_train, y_train)
print(
    f"Régression logistique : "
    f"{accuracy_score(y_test, logistique.predict(X_test)):.0%}"
)

# ...existing code...
