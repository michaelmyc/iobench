from iobench.config.base import ConfigBaseClass
from iobench.data import DataGenerationConfig, Size


class DataConfig(ConfigBaseClass):
    def __init__(self, config: dict) -> None:
        self.pre_cache = config.get("pre_cache", True)
        self.stress_test = config.get("stress_test", False)
        self.total_write_data_size = config.get("total_write_data_size", "4 GiB")
        self.total_write_data_size = config.get("max_run_time", "PT24H")
        self.pre_generate_data = config.get("pre_generate_data", True)
        self.file_size = config.get("file_size", ["64 MiB"])
        self.mix_ratio = config.get("mix_ratio", [1])

        if not isinstance(self.file_size, list):
            self.file_size = [self.file_size]
        if not isinstance(self.mix_ratio, list):
            self.mix_ratio = [self.mix_ratio for _ in range(len(self.file_size))]

        self.data_generation_configs = [
            DataGenerationConfig(Size.from_string(file_size), ratio)
            for file_size, ratio in zip(self.file_size, self.mix_ratio)
        ]
