#!/usr/bin/env python3
import pyperf
from sequential import remote_api_task, image_rotate_task
from asyncronous import remote_api_task_bad as async_remote_api_bad
from asyncronous import remote_api_task_good as async_remote_api_good
from asyncronous import rotate_image_task as async_image_rotate_task
from concurrent_threads import remote_api_task as threaded_remote_api_task
from concurrent_threads import rotate_image_task as threaded_image_rotate_task
from concurrent_processes import remote_api_task as multiprocess_remote_api_task
from concurrent_processes import rotate_image_task as multiprocess_image_rotate_task

runner = pyperf.Runner()

def run_suite():
    runner.bench_func("Sequential IO heavy processing", remote_api_task, 50),
    runner.bench_async_func("Falsely-asyncronous IO heavy processing", async_remote_api_bad, 50),
    runner.bench_async_func("Truly-asyncronous IO heavy processing", async_remote_api_good, 50),
    runner.bench_func("Threaded IO heavy processing (8 threads)", threaded_remote_api_task, 50, 8),

    runner.bench_func("Threaded IO heavy processing (32 threads)", threaded_remote_api_task, 50, 32),
    runner.bench_func("Threaded IO heavy processing (256 threads)", threaded_remote_api_task, 50, 256),
    runner.bench_func("Threaded IO heavy processing (1024 threads)", threaded_remote_api_task, 50, 1024),

    runner.bench_func("Multiprocessed IO heavy processing (1 process, 1 item per task)", multiprocess_remote_api_task, 50, 1, 1),
    runner.bench_func("Multiprocessed IO heavy processing (2 processes, 1 item per task)", multiprocess_remote_api_task, 50, 1, 2),
    runner.bench_func("Multiprocessed IO heavy processing (8 processes, 1 item per task)", multiprocess_remote_api_task, 50, 1, 8),
    runner.bench_func("Multiprocessed IO heavy processing (32 processes, 1 item per task)", multiprocess_remote_api_task, 50, 1, 32),
    runner.bench_func("Multiprocessed IO heavy processing (1 process, 5 items per task)", multiprocess_remote_api_task, 50, 5, 1),
    runner.bench_func("Multiprocessed IO heavy processing (2 processes, 5 items per task)", multiprocess_remote_api_task, 50, 5, 2),
    runner.bench_func("Multiprocessed IO heavy processing (8 processes, 5 items per task)", multiprocess_remote_api_task, 50, 5, 8),
    runner.bench_func("Multiprocessed IO heavy processing (32 processes, 5 items per task)", multiprocess_remote_api_task, 50, 5, 32),

    runner.bench_func("Sequential CPU heavy processing", image_rotate_task, 10, 64),
    runner.bench_async_func("Asyncronous CPU heavy processing", async_image_rotate_task, 10, 64),

    runner.bench_func("Threaded CPU heavy processing (2 threads, 64 images)", threaded_image_rotate_task, 10, 64, 2),
    runner.bench_func("Threaded CPU heavy processing (8 threads, 64 images)", threaded_image_rotate_task, 10, 64, 8),
    runner.bench_func("Threaded CPU heavy processing (32 threads, 64 images)", threaded_image_rotate_task, 10, 64, 32),
    runner.bench_func("Threaded CPU heavy processing (64 threads, 64 images)", threaded_image_rotate_task, 10, 64, 64),

    # Some threads are unoccupied
    runner.bench_func("Threaded CPU heavy processing (128 threads, 64 images)", threaded_image_rotate_task, 10, 64, 128),

    runner.bench_func("Multiprocessed CPU heavy processing (2 processes, 64 images)", multiprocess_image_rotate_task, 10, 64, 2),
    runner.bench_func("Multiprocessed CPU heavy processing (4 processes, 64 images)", multiprocess_image_rotate_task, 10, 64, 4),
    runner.bench_func("Multiprocessed CPU heavy processing (8 processes, 64 images)", multiprocess_image_rotate_task, 10, 64, 8),
    runner.bench_func("Multiprocessed CPU heavy processing (16 processes, 64 images)", multiprocess_image_rotate_task, 10, 64, 16),
    runner.bench_func("Multiprocessed CPU heavy processing (32 processes, 64 images)", multiprocess_image_rotate_task, 10, 64, 32),
    # Some processes are unoccupied
    runner.bench_func("Multiprocessed CPU heavy processing (128 processes, 64 images)", multiprocess_image_rotate_task, 10, 64, 128),

if __name__ == "__main__":
    run_suite()
