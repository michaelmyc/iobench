import grpc

import iobench.grpc.iobench_pb2 as iobench_pb2
import iobench.grpc.iobench_pb2_grpc as iobench_pb2_grpc


def run():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = iobench_pb2_grpc.IOBenchStub(channel)

        for request in [
            iobench_pb2.ClientMessage(data=f"Request {i+1}") for i in range(5)
        ]:

            # Call the Benchmark method with the generator
            response = stub.Benchmark(request)

            # Process the responses
            print(f"Client received: {response.result}")


def build(x):
    for t in x:
        yield t


def test():
    pass
    # x = [iobench_pb2.ClientMessage(data=f"Request {i+1}") for i in range(5)]
    # print(build(x)


if __name__ == "__main__":
    run()
    # test()
