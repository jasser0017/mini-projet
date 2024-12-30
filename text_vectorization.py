from sklearn.feature_extraction.text import TfidfVectorizer

stop_words_french = set([
    'a', 'à', 'abord', 'afin', 'après', 'aucun', 'aucune', 'au', 'aucune', 'avant', 'avec', 'avoir', 'bien', 'car', 'ce', 'ces',
    'ceci', 'cela', 'ces', 'chez', 'comme', 'comment', 'dans', 'de', 'des', 'du', 'elle', 'elles', 'en', 'encore', 'etre', 'étant',
    'être', 'eu', 'fait', 'faire', 'faites', 'ils', 'il', 'la', 'le', 'les', 'leur', 'leurs', 'lors', 'lui', 'ma', 'mais', 'me', 
    'même', 'mes', 'mine', 'moins', 'mon', 'n\'', 'ne', 'ni', 'non', 'nos', 'notre', 'nous', 'ou', 'oui', 'par', 'parce', 'pas',
    'pour', 'pourquoi', 'quand', 'que', 'quel', 'quelle', 'quelles', 'quelques', 'qui', 'quoi', 'rester', 'sans', 'se', 'ses',
    'soi', 'soi-même', 'sont', 'sur', 'si', 'ta', 'tant', 'te', 'tes', 'ton', 'tous', 'tout', 'trop', 'très', 'un', 'une', 'votre',
    'vous', 'vu', 'y', 'être'
])

# Fonction de vectorisation TF-IDF
def vectorize_text(faq_dataset):
    tfidf_vectorizer = TfidfVectorizer(stop_words='english')
    questions = [faq["question"] for faq in faq_dataset]
    faq_vectors = tfidf_vectorizer.fit_transform(questions)
    return tfidf_vectorizer, faq_vectors
