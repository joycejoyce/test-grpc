# grpc_client.py
import grpc
import demo_pb2, demo_pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = demo_pb2_grpc.CalculatorStub(channel)
    resp = stub.Add(demo_pb2.AddRequest(a=123, b=456))
    print("gRPC Add result:", resp.result)

if __name__ == '__main__':
    run()
