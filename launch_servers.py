import subprocess

def launch_servers():
    try:
        # Launch gRPC server
        grpc_process = subprocess.Popen(['python', 'grpc_server.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("gRPC server started.")

        # Launch REST server
        rest_process = subprocess.Popen(['python', 'rest_server.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("REST server started.")

        # Wait for both processes to complete (optional)
        grpc_process.wait()
        rest_process.wait()

    except KeyboardInterrupt:
        print("\nShutting down servers...")
        grpc_process.terminate()
        rest_process.terminate()

if __name__ == '__main__':
    launch_servers()