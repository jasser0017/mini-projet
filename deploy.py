from flask import Flask, request, jsonify
from data_preparation import prepare_data
from text_vectorization import vectorize_text
from similarity_calculation import calculate_similarity
from answer_selection import select_best_answer

app = Flask(__name__)

# Charger et préparer les données
faq_dataset = prepare_data()
tfidf_vectorizer, faq_vectors = vectorize_text(faq_dataset)

@app.route('/faq', methods=['GET'])
def faq():
    user_query = request.args.get('question')
    if user_query:
        similarities = calculate_similarity(user_query, tfidf_vectorizer, faq_vectors)
        answer = select_best_answer(similarities, faq_dataset)
        return jsonify({"answer": answer})
    else:
        return jsonify({"error": "Question not provided"}), 400

if __name__ == '__main__':
    app.run(debug=True)
