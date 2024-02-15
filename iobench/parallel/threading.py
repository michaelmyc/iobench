import threading
from typing import Any, Callable, List

from tqdm.auto import tqdm

from iobench.parallel.base import ParallelExecutor, ParallelTask


class ThreadedExecutor(ParallelExecutor):
    def __init__(self, max_concurrency: int = 16, disable_tqdm: bool = False) -> None:
        self.sem = threading.Semaphore(max_concurrency)
        self.lock = threading.Lock()
        self.disable_tqdm = disable_tqdm
        self.threads = []
        self.results = []

    def _task_wrapper(self, task: ParallelTask) -> Callable[[], Any]:
        def wrapped_func():
            with self.sem:
                result = task.func(*task.args, **task.kwargs)
                with self.lock:
                    self.results.append(result)
                    self.pbar.update(1)

        return wrapped_func

    def add_task(self, task: ParallelTask) -> None:
        thread = threading.Thread(target=self._task_wrapper(task))
        self.threads.append(thread)

    def run_tasks(self) -> List[Any]:
        with tqdm(total=len(self.threads), disable=self.disable_tqdm) as self.pbar:
            for thread in self.threads:
                thread.start()
            for thread in self.threads:
                thread.join()
        return self.results
