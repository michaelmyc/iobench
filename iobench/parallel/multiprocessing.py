import multiprocessing
from typing import Any, List

from tqdm.auto import tqdm

from iobench.parallel.base import ParallelExecutor, ParallelTask


class MultiprocessExecutor(ParallelExecutor):
    def __init__(self, max_concurrency: int = 16, disable_tqdm: bool = False) -> None:
        self.max_concurrency = max_concurrency
        self.disable_tqdm = disable_tqdm
        self.tasks = []

    def add_task(self, task: ParallelTask) -> None:
        self.tasks.append(task)

    def run_tasks(self) -> List[Any]:
        results = []
        with multiprocessing.Pool(self.max_concurrency) as p:
            with tqdm(total=len(self.tasks), disable=self.disable_tqdm) as pbar:
                for task in self.tasks:
                    result = p.apply_async(
                        task.func,
                        args=task.args,
                        kwds=task.kwargs,
                        callback=lambda _: pbar.update(1),
                    )
                    results.append(result)
                results = [result.get() for result in results]
        return results
