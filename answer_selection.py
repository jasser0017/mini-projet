import numpy as np

# Fonction pour sélectionner la meilleure réponse
def select_best_answer(similarities, faq_dataset):
    best_match_idx = np.argmax(similarities)
    return faq_dataset[best_match_idx]["answer"]
