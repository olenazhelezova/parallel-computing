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

```
Concurrency/asyncronousy benchmark


Benchmark                                                              Mean time (sec)  Memory
-------------------------------------------------------------------  -----------------  ----------
Sequential IO heavy processing                                                  21.33   37.938MiB
Falsely-asyncronous IO heavy processing                                         22.588  37.531MiB
Truly-asyncronous IO heavy processing                                            1.043  38.797MiB
Threaded IO heavy processing (8 threads)                                         3.353  37.734MiB
Threaded IO heavy processing (32 threads)                                        1.223  39.000MiB
Threaded IO heavy processing (256 threads)                                       0.962  39.906MiB
Threaded IO heavy processing (1024 threads)                                      0.95   39.688MiB
Multiprocessed IO heavy processing (1 process, 1 item per task)                 22.852  38.406MiB
Multiprocessed IO heavy processing (2 processes, 1 item per task)               11.839  38.578MiB
Multiprocessed IO heavy processing (8 processes, 1 item per task)                3.665  38.391MiB
Multiprocessed IO heavy processing (32 processes, 1 item per task)               2.123  38.203MiB
Multiprocessed IO heavy processing (1 process, 5 items per task)                22.63   38.281MiB
Multiprocessed IO heavy processing (2 processes, 5 items per task)              11.909  38.062MiB
Multiprocessed IO heavy processing (8 processes, 5 items per task)               4.1    37.672MiB
Multiprocessed IO heavy processing (32 processes, 5 items per task)              3.095  38.062MiB
Sequential CPU heavy processing                                                 42.885  633.562MiB
Asyncronous CPU heavy processing                                                43.453  617.734MiB
Threaded CPU heavy processing (2 threads, 64 images)                            42.136  629.109MiB
Threaded CPU heavy processing (8 threads, 64 images)                            42.149  607.719MiB
Threaded CPU heavy processing (32 threads, 64 images)                           43.392  613.156MiB
Threaded CPU heavy processing (64 threads, 64 images)                           42.613  617.578MiB
Threaded CPU heavy processing (128 threads, 64 images)                          42.538  612.422MiB
Multiprocessed CPU heavy processing (2 processes, 64 images)                    23.868  1.470GiB
Multiprocessed CPU heavy processing (4 processes, 64 images)                    16.715  1.429GiB
Multiprocessed CPU heavy processing (8 processes, 64 images)                    14.871  1.520GiB
Multiprocessed CPU heavy processing (16 processes, 64 images)                   14.933  1.424GiB
Multiprocessed CPU heavy processing (32 processes, 64 images)                   15.529  1.369GiB
Multiprocessed CPU heavy processing (128 processes, 64 images)                  16.708  1.335GiB

Platform: macOS-15.2-arm64-arm-64bit-Mach-O
CPU Count: 8
pyperf version: 2.8.1
python version: cpython3.13.1 (64-bit) revision 06714517797
```

