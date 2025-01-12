from flask import Flask, request, jsonify

app = Flask(__name__)  # double underscores

@app.route('/')
def home():
    return "Hello from Docker Container!"  # Change back to original message

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    amount = data.get('loan_amount', 0)
    # Simple logic: approve if amount <= 100000
    result = 'approved' if amount <= 100000 else 'rejected'
    return jsonify({'result': result})

if __name__ == "__main__":  # double underscores
    app.run(debug=True, host='0.0.0.0')