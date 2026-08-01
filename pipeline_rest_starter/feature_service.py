import requests
import time

MODEL_SERVICE_URL = "http://localhost:5001/predict"

def call_model_service(features, shape):
    start_time = time.time()
    payload = {"features": features, "shape": shape}
    
    # REST call to model service
    response = requests.post(MODEL_SERVICE_URL, json=payload)
    latency = (time.time() - start_time) * 1000
    return response.json(), latency

if __name__ == "__main__":
    sample_features = [0.1 * i for i in range(1000)]
    sample_shape = [1, 1000]
    result, lat = call_model_service(sample_features, sample_shape)
    print(f"REST Response: {result}, Latency: {lat:.2f} ms")
