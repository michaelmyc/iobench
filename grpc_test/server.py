# server.py

import time
from concurrent import futures

import grpc
import streaming_example_pb2
import streaming_example_pb2_grpc


class StreamingExampleServicer(streaming_example_pb2_grpc.StreamingExampleServicer):
    def BidirectionalStream(self, request_iterator, context):
        for request in request_iterator:
            response = streaming_example_pb2.Response()
            response.message = f"Server received: {request.message}"
            print(f"Server received: {request.message}")
            yield response


def serve(max_worksers: int = 10):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=max_worksers))
    streaming_example_pb2_grpc.add_StreamingExampleServicer_to_server(
        StreamingExampleServicer(), server
    )
    server.add_insecure_port("[::]:50051")
    server.start()
    print("Server started")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
