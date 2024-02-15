import tomllib
from os import PathLike
from pathlib import Path
from typing import Any, Union

from iobench.config.benchmark import BenchmarkConfig
from iobench.config.concurrency import ConcurrencyConfig
from iobench.config.data import DataConfig
from iobench.config.io import IOConfig


class Config:
    def __init__(self, fpath: Union[PathLike, bytes, str]) -> None:
        self._fpath = Path(fpath)
        self.load_config()
        self.parse_config()

    def load_config(self) -> None:
        with open(self._fpath, "rb") as f:
            self._config = tomllib.load(f)

    def parse_config(self) -> None:
        self.data = DataConfig(self._config["data"])
        self.io = IOConfig(self._config["io"])
        self.benchmark = BenchmarkConfig(self._config["benchmark"])
        self.concurrency = ConcurrencyConfig(self._config["concurrency"])

    def __str__(self) -> str:
        return "\n".join(
            [
                "===== Concurrency =====",
                str(self.concurrency),
                "========= Data ========",
                str(self.data),
                "========== IO =========",
                str(self.io),
                "====== Benchmark ======",
                str(self.benchmark),
            ]
        )

    def __repr__(self) -> str:
        return f'Config("{self._fpath}")'
