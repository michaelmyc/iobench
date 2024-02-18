from iobench.config.base import ConfigBaseClass


class DataConfig(ConfigBaseClass):
    def __init__(self, config: dict) -> None:
        self.total_data_size = config.get("total_data_size", "4 GiB")
        self.pre_generate_data = config.get("pre_generate_data", True)
        self.file_size = config.get("file_size", ["64 MiB"])
        self.mix_ratio = config.get("mix_ratio", [1])

        if not isinstance(self.file_size, list):
            self.file_size = [self.file_size]
        if not isinstance(self.mix_ratio, list):
            self.mix_ratio = [self.mix_ratio for _ in range(len(self.file_size))]
