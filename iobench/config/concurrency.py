from iobench.config.base import ConfigBaseClass, StrEnum


class ParallelMethod(StrEnum):
    Threading = "Threading"
    Multiprocessing = "Multiprocessing"


class ConcurrencyConfig(ConfigBaseClass):
    def __init__(self, config: dict) -> None:
        self.parallel_method: ParallelMethod = ParallelMethod(
            config.get("parallel_method", "Threading")
        )
        self.max_concurrency = config.get("max_concurrency", 16)
        self.nodes = config.get("nodes", ["localhost"])
        self.master_node = config.get("master_node", "localhost")
