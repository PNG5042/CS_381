
from flask import Flask, request, jsonify

app = Flask(__name__)

reviews = []

@app.route('/review', methods=['POST'])
def add_review():
    data = request.get_json()
    reviews.append(data)
    return jsonify({"status": "Review submitted"}), 201

@app.route('/reviews', methods=['GET'])
def get_reviews():
    return jsonify(reviews), 200

if __name__ == '__main__':
    app.run(debug=True)
