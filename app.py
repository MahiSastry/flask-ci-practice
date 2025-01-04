from flask import Flask, request, jsonify

app = Flask(__name__)  # double underscores

@app.route('/')
def home():
    return "Different message!"  # This should fail our test

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()  # get_json() not getjson()
    # Simple logic
    amount = data.get('loan_amount', 0)  # loan_amount to match our test case
    return jsonify({'result': 'approved' if amount < 100000 else 'rejected'})

if __name__ == "__main__":  # double underscores
    app.run(debug=True, host='0.0.0.0')