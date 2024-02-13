from pathlib import Path
from typing import Any, Union

from yaml import load

from .benchmark import BenchmarkConfig
from .data import DataConfig
from .io import IOConfig

try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader


class Config:
    def __init__(self, fpath: Union[Path, str]) -> None:
        self._fpath = Path(fpath)
        self.load_config()
        self.parse_config()

    def load_config(self) -> None:
        with open(self._fpath) as f:
            self._config = load(f.read(), Loader=Loader)

    def parse_config(self) -> None:
        self.data = DataConfig(self._config["data"])
        self.io = IOConfig(self._config["io"])
        self.benchmark = BenchmarkConfig(self._config["benchmark"])

    def __str__(self) -> str:
        return "\n".join(
            [
                "======== Data ========",
                str(self.data),
                "========= IO =========",
                str(self.io),
                "====== Benchmark =====",
                str(self.benchmark),
            ]
        )

    def __repr__(self) -> str:
        return f'Config("{self._fpath}")'