import io
import random
from dataclasses import dataclass
from typing import List

import numpy as np

from iobench.data.units import BaseUnit, Size


@dataclass
class DataGenerationConfig:
    size: Size
    ratio: float


class DataGenerator:
    def __init__(self, gen_configs: List[DataGenerationConfig]) -> None:
        self.configs = gen_configs

    def _random_config(self) -> DataGenerationConfig:
        return random.choices(
            self.configs, weights=[cfg.ratio for cfg in self.configs]
        )[0]

    def _generate_data(self, size: Size) -> np.ndarray:
        n_bytes = size.to_bytes()
        n_floats = int((n_bytes - 128) / 8)
        return np.random.rand(n_floats)

    def generate_data(self) -> io.BytesIO:
        f = io.BytesIO()
        config = self._random_config()
        array = self._generate_data(config.size)
        np.save(f, array)
        return f
