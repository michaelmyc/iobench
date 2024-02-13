from yaml import dump

try:
    from yaml import CDumper as Dumper
except ImportError:
    from yaml import Dumper


class DataConfig:
    def __init__(self, config: dict) -> None:
        self.use_cache: bool = config.get("use_cache", False)
        self.cache_data: bool = config.get("save_cache", False)
        self.cache_dir: str = config.get("cache_dir", "")

    def __str__(self) -> str:
        str_dict = {k: str(v) for k, v in self.__dict__.items()}
        return dump(str_dict, allow_unicode=True, Dumper=Dumper)

    def __repr__(self) -> str:
        return str(self.__dict__)
