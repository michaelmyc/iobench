import time

import grpc
import streaming_example_pb2
import streaming_example_pb2_grpc


def run():
    channel = grpc.insecure_channel("localhost:50051")
    stub = streaming_example_pb2_grpc.StreamingExampleStub(channel)

    def generate_messages():
        messages = ["Message 1", "Message 2", "Message 3"]
        for message in messages:
            request = streaming_example_pb2.Request()
            request.message = message
            time.sleep(1)
            yield request

    responses = stub.BidirectionalStream(generate_messages())
    for response in responses:
        print(f"Client received: {response.message}")


if __name__ == "__main__":
    run()
