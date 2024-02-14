from iobench.config.base import ConfigBaseClass


class DataConfig(ConfigBaseClass):
    def __init__(self, config: dict) -> None:
        self.use_cache: bool = config.get("use_cache", False)
        self.cache_data: bool = config.get("save_cache", False)
        self.cache_dir: str = config.get("cache_dir", "")
