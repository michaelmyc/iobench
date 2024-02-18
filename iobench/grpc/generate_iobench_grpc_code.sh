#!/usr/bin/env bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

python -m grpc_tools.protoc -I$SCRIPT_DIR --python_out=$SCRIPT_DIR --grpc_python_out=$SCRIPT_DIR iobench.proto