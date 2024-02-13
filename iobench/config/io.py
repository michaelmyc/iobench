from enum import Enum
from typing import Union

from yaml import dump

try:
    from yaml import CDumper as Dumper
except ImportError:
    from yaml import Dumper


class IOType(str, Enum):
    File = "File"
    S3 = "S3"

    def __repr__(self) -> str:
        return self.value

    def __str__(self) -> str:
        return self.value


class IOConfig:
    def __init__(self, config: dict) -> None:
        self.io_type: IOType = IOType(config.get("io_type", "File"))
        self.io_config: Union[S3Config, FileConfig, None] = None
        if self.io_type is IOType.S3:
            self.io_config = S3Config(config.get("s3_config", {}))
        elif self.io_type is IOType.File:
            self.io_config = FileConfig(config.get("file_config", {}))

    def __str__(self) -> str:
        str_dict = {k: str(v) for k, v in self.__dict__.items()}
        return dump(str_dict, allow_unicode=True, Dumper=Dumper)

    def __repr__(self) -> str:
        return str(self.__dict__)


class S3Config:
    def __init__(self, config: dict) -> None:
        assert "user" in config or "access_key" in config
        assert "password" in config or "secret_key" in config
        if "user" in config:
            self.access_key = config["user"]
        else:
            self.access_key = config["access_key"]
        if "password" in config:
            self.secret_key = config["password"]
        else:
            self.secret_key = config["secret_key"]

        # TODO
        pass


class FileConfig:
    def __init__(self, config: dict) -> None:
        # TODO
        pass
