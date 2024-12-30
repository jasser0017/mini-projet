from sklearn.metrics.pairwise import cosine_similarity

# Fonction pour calculer la similarité cosinus
def calculate_similarity(user_query, tfidf_vectorizer, faq_vectors):
    # Transformer la question de l'utilisateur en vecteur TF-IDF
    user_query_vector = tfidf_vectorizer.transform([user_query])
    
    # Calcul de la similarité cosinus entre la question de l'utilisateur et les questions FAQ
    similarities = cosine_similarity(user_query_vector, faq_vectors).flatten()
    
    return similarities
