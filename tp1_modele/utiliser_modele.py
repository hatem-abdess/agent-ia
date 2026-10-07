import joblib
import pandas as pd

modele = joblib.load("modele_clients.pkl")

client = pd.DataFrame({
    "anciennete_mois": [12],
    "nb_achats": [5],
    "montant_moyen": [120.0],
    "reclamations": [3],
})

print("Prédiction :", modele.predict(client)[0])

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