from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    features = data.get("features", [])
    shape = data.get("shape", [])
    
    # Simple mock inference calculation
    scores = [f * 2.0 for f in features]
    return jsonify({"scores": scores, "model_version": "1.0-rest"})

if __name__ == "__main__":
    app.run(port=5001)
