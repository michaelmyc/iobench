from abc import ABCMeta, abstractmethod
from pathlib import Path


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class IO(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, concurrency: int, disable_tqdm: bool) -> None:
        pass

    @abstractmethod
    def read(self, task: ParallelTask) -> None:
        pass

    @abstractmethod
    def write(self) -> List[Any]:
        pass
