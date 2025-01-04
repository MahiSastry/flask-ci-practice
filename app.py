from flask import Flask, request, jsonify

app = Flask(__name__)  # double underscores

@app.route('/')
def home():
    return "Hello from Docker Container!"  # Change back to original message

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    amount = data.get('loan_amount', 0)
    # Let's change logic to always approve
    return jsonify({'result': 'approved'})

if __name__ == "__main__":  # double underscores
    app.run(debug=True, host='0.0.0.0')