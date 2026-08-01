import grpc
from concurrent import futures
import postproc_pb2
import postproc_pb2_grpc

class PostProcessorServicer(postproc_pb2_grpc.PostProcessorServicer):
    def Process(self, request, context):
        formatted = [f"Class_{idx}: {score:.4f}" for idx, score in enumerate(request.scores)]
        return postproc_pb2.PostProcResponse(
            formatted_predictions=formatted,
            success=True
        )

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    postproc_pb2_grpc.add_PostProcessorServicer_to_server(PostProcessorServicer(), server)
    server.add_insecure_port('[::]:50052')
    server.start()
    print("gRPC PostProcessor Server running on port 50052...")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
