# benchmark.py
import time
import grpc
import requests
import demo_pb2, demo_pb2_grpc
from datetime import datetime

def log_with_timestamp(message):
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]}] {message}")

def grpc_latency(runs=1000):
    log_with_timestamp("grpc_latency - start")
    channel = grpc.insecure_channel('localhost:50051')
    stub = demo_pb2_grpc.CalculatorStub(channel)
    # warm-up
    stub.Add(demo_pb2.AddRequest(a=1, b=1))

    start = time.perf_counter()
    for i in range(1, runs + 1):
        response = stub.Add(demo_pb2.AddRequest(a=123, b=456))
        log_with_timestamp(f"gRPC progress: {i}/{runs}, response: {response}")
    total = time.perf_counter() - start
    log_with_timestamp("grpc_latency - end")  # newline after loop
    return total, total / runs

def rest_latency(runs=1000):
    log_with_timestamp("rest_latency - start")
    url = 'http://localhost:5000/add'
    # warm-up
    requests.post(url, json={'a':1, 'b':1})

    start = time.perf_counter()
    for i in range(1, runs + 1):
        response = requests.post(url, json={'a':123, 'b':456})
        log_with_timestamp(f"REST progress: {i}/{runs}, response: {response.json()}")
    total = time.perf_counter() - start
    log_with_timestamp("rest_latency - end")  # newline after loop
    return total, total / runs

if __name__ == '__main__':
    runs = 5
    grpc_total, grpc_avg = grpc_latency(runs)
    rest_total, rest_avg = rest_latency(runs)

    log_with_timestamp(f"\ngRPC  [{runs} calls]: total {grpc_total:.3f}s, avg {grpc_avg*1000:.2f} ms")
    log_with_timestamp(f"REST  [{runs} calls]: total {rest_total:.3f}s, avg {rest_avg*1000:.2f} ms")