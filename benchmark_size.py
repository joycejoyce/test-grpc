# size_compare.py
import json
from demo_pb2 import AddRequest

# Prepare
grpc_req = AddRequest(a=123, b=456)
json_str = json.dumps({'a': 123, 'b': 456})

# Measure
print("gRPC message size:", grpc_req.ByteSize(), "bytes")
print("JSON message size:", len(json_str.encode()), "bytes")
