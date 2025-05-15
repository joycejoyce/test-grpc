# grpc_server.py
from concurrent import futures
import grpc
import demo_pb2, demo_pb2_grpc

class CalculatorServicer(demo_pb2_grpc.CalculatorServicer):
    def Add(self, request, context):
        # Strongly-typed, binary-serialized
        return demo_pb2.AddReply(result=request.a + request.b)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    demo_pb2_grpc.add_CalculatorServicer_to_server(CalculatorServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
