faq = {
    "horaires": "Nous sommes ouverts du lundi au vendredi, de 8h à 17h.",
    "congé": "Chaque employé a droit à 30 jours de congés par an.",
    "contact": "Écrivez à rh@entreprise.tn pour toute question RH.",
}


def calculer(expression):
    try:
        return f"Résultat : {eval(expression)}"
    except Exception:
        return "Je n'ai pas compris le calcul."


def repondre(question):
    question = question.lower()

    if question in ["bonjour", "salut", "salam"]:
        return "Bonjour ! Je suis votre assistant. Posez-moi une question."
    elif question.startswith("calcul"):
        expression = question.replace("calcul", "").strip()
        return calculer(expression)

    for mot_cle, reponse in faq.items():
        if mot_cle in question:
            return reponse

    return "Désolé, je ne connais pas encore la réponse."


print("=== Mini-assistant RH (tapez 'quit' pour sortir) ===")

while True:
    question = input("Vous : ")

    if question.lower() == "quit":
        print("Assistant : Au revoir !")
        break

    print("Assistant :", repondre(question))