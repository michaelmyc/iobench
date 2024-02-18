import time
from concurrent import futures

import grpc

import iobench.grpc.iobench_pb2 as iobench_pb2
import iobench.grpc.iobench_pb2_grpc as iobench_pb2_grpc


class IOBenchService(iobench_pb2_grpc.IOBenchServicer):
    def Heartbeat(self, request, context):
        # Process the incoming request and send a response
        response = iobench_pb2.HeartbeatResponse()
        response.terminate = False
        return response

    def Communicate(self, request_generator, context):
        # Process the incoming request and send a response
        for request in request_generator:
            response = iobench_pb2.ServerMessage()
            response.result = f"Received: {request.data}"
            return response


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    iobench_pb2_grpc.add_IOBenchServicer_to_server(IOBenchService(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    print("Server started on port 50051")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
