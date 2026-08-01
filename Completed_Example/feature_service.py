import grpc
import time
import model_pb2
import model_pb2_grpc

def run_grpc_inference():
    # Connect to the gRPC Model Server on port 50051
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = model_pb2_grpc.ModelServiceStub(channel)
        
        # Prepare mock tensor payload (1000 float features)
        sample_features = [0.1 * i for i in range(1000)]
        sample_shape = [1, 1000]
        
        request = model_pb2.PredictRequest(
            features=sample_features,
            shape=sample_shape,
            request_id="req-001"
        )
        
        start_time = time.time()
        response = stub.Predict(request)
        latency = (time.time() - start_time) * 1000
        
        print(f"[gRPC] Model Version: {response.model_version}")
        print(f"[gRPC] Returned {len(response.scores)} prediction scores.")
        print(f"[gRPC] Latency: {latency:.2f} ms")

if __name__ == "__main__":
    run_grpc_inference()
