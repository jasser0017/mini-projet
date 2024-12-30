import re

# Exemple de jeu de données de FAQ
faq_dataset = [
    {"question": "Quel est votre politique de retour ?", "answer": "Vous pouvez retourner tout article dans les 30 jours suivant l'achat."},
    {"question": "Comment puis-je suivre ma commande ?", "answer": "Vous pouvez suivre votre commande en utilisant le numéro de suivi fourni dans l'email de confirmation."},
    {"question": "Offrez-vous la livraison gratuite ?", "answer": "Oui, nous offrons la livraison gratuite sur les commandes de plus de 50€."},
    {"question": "Comment contacter le service client ?", "answer": "Vous pouvez nous contacter via notre formulaire de contact ou en appelant notre ligne de service client."},
    {"question": "Quels modes de paiement acceptez-vous ?", "answer": "Nous acceptons les cartes de crédit, PayPal et Apple Pay."},
    {"question": "Où êtes-vous situés ?", "answer": "Notre siège social est basé à Paris, France."},
    {"question": "Puis-je modifier ma commande après l'avoir passée ?", "answer": "Vous pouvez modifier votre commande dans les 30 minutes suivant la validation en contactant le service client."},
    {"question": "Comment retourner un article ?", "answer": "Pour retourner un article, connectez-vous à votre compte et demandez un retour via notre portail de retours."},
    {"question": "Mes informations personnelles sont-elles sécurisées ?", "answer": "Oui, nous utilisons le cryptage pour protéger vos informations personnelles et de paiement."},
    {"question": "Offrez-vous des cartes cadeaux ?", "answer": "Oui, nous offrons des cartes cadeaux numériques qui peuvent être utilisées sur notre site."}
]

# Nettoyage de texte (suppression des caractères spéciaux et des espaces inutiles)
def clean_text(text):
    text = text.lower()  # Mettre en minuscule
    text = re.sub(r'\s+', ' ', text)  # Suppression des espaces multiples
    text = re.sub(r'[^\w\s]', '', text)  # Suppression des caractères spéciaux
    return text

# Nettoyer les questions et réponses
def prepare_data():
    return [
        {"question": clean_text(faq["question"]), "answer": clean_text(faq["answer"])} for faq in faq_dataset
    ]
