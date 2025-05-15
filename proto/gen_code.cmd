python -m grpc_tools.protoc -I=. --python_out=. --grpc_python_out=. demo.proto

REM Rename the generated files
@REM rename demo_pb2.py demo_pb3.py
@REM rename demo_pb2_grpc.py demo_pb3_grpc.py