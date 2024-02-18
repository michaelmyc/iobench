import minio

from iobench.io.base import Singleton


class MinIO(metaclass=Singleton):
    def __init__(self) -> None:
        self.client = minio.Minio(endpoint=x, access_key=ak, secret_key=sk, secure=ssl)
