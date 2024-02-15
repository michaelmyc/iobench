from abc import ABCMeta, abstractmethod
from typing import Any, Callable, List


class ParallelTask:
    def __init__(self, func: Callable, *args: Any, **kwargs: Any):
        self.func = func
        self.args = args
        self.kwargs = kwargs


class ParallelExecutor(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, max_concurrency: int, disable_tqdm: bool) -> None:
        pass

    @abstractmethod
    def add_task(self, task: ParallelTask) -> None:
        pass

    @abstractmethod
    def run_tasks(self) -> List[Any]:
        pass
