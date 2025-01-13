# Benchmarking async/concurrent approaches

This is an educational project aimed to explore asyncronous and concurrent approaches to solving problems, as well as comparing productivity for different types of jobs. The endgoal is to gather knowledge and intuition to be able to effectively leverage it in my future projects. 

The 2 sample workloads explored are: 
- Simulation of network IO-heavy tasks like batch processing of records from remote API (with sleep to network/remote server delays)
- Simulation of CPU-heavy computationally intensite task via image processing (rotation) 

With following approaches: 
- Plain sequential processing
- Asyncronous approach (if applicable)
- Thread-distributed task processing (with varying number of threads)
- Process-distributed task processing (with varying number of processes)

## Usage

1. Clone the project and install the dependencies

2. To obtain the results you will first need to run the benchmarking suite
    ./bench.py -o bench_data.json
> **_NOTE:_** This is built using [pyperf](https://github.com/psf/pyperf) module, so you can adjust your benchmark using [pyperf CLI arguments](https://pyperf.readthedocs.io/en/latest/runner.html). The fastest one ought to be ```-l 1 -p 1 -w 1```

3. Subsequently, the raw data produced by benchmark will appear in the output file. In order to format it, you can run
    ./main.py 
> **_NOTE:_** Currently the filename used for generation in main.py is hardcoded to ```bench_data.json``` ¯\_(ツ)_/¯

Which should produce the output like this: 

### With GIL enabled

```
Concurrency/asyncronousy benchmark


Benchmark                                                                     Mean time (sec)  Memory
--------------------------------------------------------------------------  -----------------  ---------
Sequential IO heavy processing                                                         22.786  41.984MiB
Falsely-asyncronous IO heavy processing                                                22.244  42.156MiB
Truly-asyncronous IO heavy processing                                                   1.135  42.297MiB
Threaded IO heavy processing (8 threads)                                                3.221  49.109MiB
Threaded IO heavy processing (32 threads)                                               1.167  68.141MiB
Threaded IO heavy processing (256 threads)                                              0.864  82.156MiB
Threaded IO heavy processing (1024 threads)                                             0.902  82.891MiB
Multiprocessed IO heavy processing (1 process, 1 item per task)                        21.591  82.891MiB
Multiprocessed IO heavy processing (2 processes, 1 item per task)                      11.706  82.891MiB
Multiprocessed IO heavy processing (8 processes, 1 item per task)                       3.442  82.891MiB
Multiprocessed IO heavy processing (32 processes, 1 item per task)                      2.412  82.891MiB
Multiprocessed IO heavy processing (1 process, 5 items per task)                       21.128  82.891MiB
Multiprocessed IO heavy processing (2 processes, 5 items per task)                     11.051  82.891MiB
Multiprocessed IO heavy processing (8 processes, 5 items per task)                      4.424  82.891MiB
Multiprocessed IO heavy processing (32 processes, 5 items per task)                     3.119  82.891MiB
Sequential CPU heavy processing (first primes 1_000_000)                              108.723  82.891MiB
Asyncronous CPU heavy processing (first primes 1_000_000)                             108.79   82.891MiB
Threaded CPU heavy processing (first primes 1_000_000) 2 threads                       57.351  82.891MiB
Threaded CPU heavy processing (first primes 1_000_000) 8 threads                       29.737  82.891MiB
Threaded CPU heavy processing (first primes 1_000_000) 16 threads                      30.067  82.891MiB
Threaded CPU heavy processing (first primes 1_000_000) 32 threads                      29.051  83.281MiB
Threaded CPU heavy processing (first primes 1_000_000) 64 threads                      28.941  84.203MiB
Multiprocessed CPU heavy processing (first primes 1_000_000) 2 processes               56.657  84.203MiB
Multiprocessed CPU heavy processing (first primes 1_000_000) 4 processes               29.935  84.203MiB
Multiprocessed CPU heavy processing (first primes 1_000_000) 8 processes               19.309  84.203MiB
Multiprocessed CPU heavy processing (first primes 1_000_000) 16 processes              18.596  84.203MiB
Multiprocessed CPU heavy processing (first primes 1_000_000) 32 processes              18.913  84.203MiB
Multiprocessed CPU heavy processing (first primes 1_000_000) 128 processes             19.33   84.203MiB

Platform: macOS-15.2-arm64-arm-64bit-Mach-O
CPU Count: 8
pyperf version: 2.8.1
python version: cpython3.13.1 (64-bit) revision 06714517797
```

### With GIL disabled

```
Concurrency/asyncronousy benchmark


Benchmark                                                                     Mean time (sec)  Memory
--------------------------------------------------------------------------  -----------------  ---------
Sequential IO heavy processing                                                         22.786  41.984MiB
Falsely-asyncronous IO heavy processing                                                22.244  42.156MiB
Truly-asyncronous IO heavy processing                                                   1.135  42.297MiB
Threaded IO heavy processing (8 threads)                                                3.221  49.109MiB
Threaded IO heavy processing (32 threads)                                               1.167  68.141MiB
Threaded IO heavy processing (256 threads)                                              0.864  82.156MiB
Threaded IO heavy processing (1024 threads)                                             0.902  82.891MiB
Multiprocessed IO heavy processing (1 process, 1 item per task)                        21.591  82.891MiB
Multiprocessed IO heavy processing (2 processes, 1 item per task)                      11.706  82.891MiB
Multiprocessed IO heavy processing (8 processes, 1 item per task)                       3.442  82.891MiB
Multiprocessed IO heavy processing (32 processes, 1 item per task)                      2.412  82.891MiB
Multiprocessed IO heavy processing (1 process, 5 items per task)                       21.128  82.891MiB
Multiprocessed IO heavy processing (2 processes, 5 items per task)                     11.051  82.891MiB
Multiprocessed IO heavy processing (8 processes, 5 items per task)                      4.424  82.891MiB
Multiprocessed IO heavy processing (32 processes, 5 items per task)                     3.119  82.891MiB
Sequential CPU heavy processing (first primes 1_000_000)                              108.723  82.891MiB
Asyncronous CPU heavy processing (first primes 1_000_000)                             108.79   82.891MiB
Threaded CPU heavy processing (first primes 1_000_000) 2 threads                       57.351  82.891MiB
Threaded CPU heavy processing (first primes 1_000_000) 8 threads                       29.737  82.891MiB
Threaded CPU heavy processing (first primes 1_000_000) 16 threads                      30.067  82.891MiB
Threaded CPU heavy processing (first primes 1_000_000) 32 threads                      29.051  83.281MiB
Threaded CPU heavy processing (first primes 1_000_000) 64 threads                      28.941  84.203MiB
Multiprocessed CPU heavy processing (first primes 1_000_000) 2 processes               56.657  84.203MiB
Multiprocessed CPU heavy processing (first primes 1_000_000) 4 processes               29.935  84.203MiB
Multiprocessed CPU heavy processing (first primes 1_000_000) 8 processes               19.309  84.203MiB
Multiprocessed CPU heavy processing (first primes 1_000_000) 16 processes              18.596  84.203MiB
Multiprocessed CPU heavy processing (first primes 1_000_000) 32 processes              18.913  84.203MiB
Multiprocessed CPU heavy processing (first primes 1_000_000) 128 processes             19.33   84.203MiB

Platform: macOS-15.2-arm64-arm-64bit-Mach-O
CPU Count: 8
pyperf version: 2.8.1
python version: cpython3.13.1 (64-bit) revision 06714517797

```

