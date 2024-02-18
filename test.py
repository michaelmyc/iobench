from iobench.config.main import Config

print(Config("test_config.toml"))

# import time

# from iobench.parallel import MultiprocessExecutor, ParallelTask, ThreadedExecutor


# def say_after(name):
#     return name


# # sem = threading.Semaphore(3)
# # results = []
# # l = threading.Lock()


# if __name__ == "__main__":
#     k = 1000
#     t = 20
#     disable = False

#     ex = ThreadedExecutor(max_concurrency=t, disable_tqdm=disable)

#     for i in range(k):
#         task = ParallelTask(say_after, i)
#         ex.add_task(task)

#     start = time.time()
#     ex.run_tasks()
#     end = time.time()

#     print(end - start)

#     ex = MultiprocessExecutor(max_concurrency=t, disable_tqdm=disable)

#     for i in range(k):
#         task = ParallelTask(say_after, i)
#         ex.add_task(task)

#     start = time.time()
#     ex.run_tasks()
#     end = time.time()

#     print(end - start)
