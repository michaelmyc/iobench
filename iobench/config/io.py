from typing import Union

from iobench.config.base import ConfigBaseClass, StrEnum


class IOType(StrEnum):
    File = "File"
    S3 = "S3"


class IOConfig(ConfigBaseClass):
    def __init__(self, config: dict) -> None:
        self.io_type: IOType = IOType(config["io_type"])
        self.io_config: Union[S3Config, FileConfig, None] = None
        if self.io_type is IOType.S3:
            self.io_config = S3Config(config["s3_config"])
        elif self.io_type is IOType.File:
            self.io_config = FileConfig(config["file_config"])


class S3Config:
    def __init__(self, config: dict) -> None:
        assert "endpoint" in config
        assert "bucket" in config
        assert "user" in config or "access_key" in config
        assert "password" in config or "secret_key" in config

        self.library = config.get("library", "minio")
        self.use_ssl = config.get("use_ssl", False)
        self.endpoint = config["endpoint"]
        self.port = config.get("port", 9000)
        self.bucket = config["bucket"]
        self.prefix = config.get("prefix", "")
        if "user" in config:
            self.access_key = config["user"]
        else:
            self.access_key = config["access_key"]
        if "password" in config:
            self.secret_key = config["password"]
        else:
            self.secret_key = config["secret_key"]


class FileConfig(ConfigBaseClass):
    def __init__(self, config: dict) -> None:
        assert "path" in config
        self.path = config["path"]
