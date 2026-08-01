import grpc
from concurrent import futures
import model_pb2
import model_pb2_grpc

class ModelServiceServicer(model_pb2_grpc.ModelServiceServicer):
    def Predict(self, request, context):
        scores = [f * 2.0 for f in request.features]
        return model_pb2.PredictResponse(scores=scores, model_version="1.0-grpc")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    model_pb2_grpc.add_ModelServiceServicer_to_server(ModelServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("gRPC Model Server running on port 50051...")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
