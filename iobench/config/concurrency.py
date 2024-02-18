import getpass
from os import PathLike
from typing import List, Union

from iobench.config.base import ConfigBaseClass, StrEnum


class ParallelMethod(StrEnum):
    Threading = "Threading"
    Multiprocessing = "Multiprocessing"


class ConcurrencyConfig(ConfigBaseClass):
    def __init__(self, config: dict) -> None:
        assert "script_path" in config

        self.parallel_method: ParallelMethod = ParallelMethod(
            config.get("parallel_method", "Threading")
        )
        self.concurrency_per_node: int = config.get("concurrency_per_node", 16)
        self.port: int = config.get("port", "50051")
        self.master_node: str = config.get("master_node", "localhost")
        self.master_db_path: str = config.get("master_db_path", "/tmp/iobench.db")
        self.nodes: List[str] = config.get("nodes", ["localhost"])
        self.script_path: Union[str, List[str]] = config["script_path"]
        self.username: Union[str, List[str]] = config.get("username", getpass.getuser())
        self.key_path: Union[PathLike, bytes, str] = config.get(
            "key_path", "~/.ssh/id_rsa"
        )

        if not isinstance(self.script_path, list):
            self.script_path = [self.script_path for _ in range(len(self.nodes))]
        if not isinstance(self.username, list):
            self.username = [self.username for _ in range(len(self.nodes))]

        assert len(self.script_path) == len(self.nodes)
        assert len(self.username) == len(self.nodes)
