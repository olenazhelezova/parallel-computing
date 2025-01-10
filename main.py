#!/usr/bin/env python3
import pyperf
from tabulate import tabulate

suite = pyperf.BenchmarkSuite.load("bench_data.json")


def sizeof_fmt(num, suffix="B"):
    for unit in ("", "Ki", "Mi", "Gi"):
        if abs(num) < 1024.0:
            return f"{num:3.3f}{unit}{suffix}"
        num /= 1024.0
    return f"{num:.1f}Yi{suffix}"


columns = ["Benchmark", "Mean time (sec)", "Memory"]
rows = []
for benchmark in suite.get_benchmarks():
    rows.append(
        [
            benchmark.get_name(),
            round(benchmark.mean(), 3),
            sizeof_fmt(benchmark.get_metadata()["mem_max_rss"]),
        ]
    )

output = "Concurrency/asyncronousy benchmark\n\n\n"
output += tabulate(rows, columns)

suite_metadata = suite.get_metadata()

output += """

Platform: {platform}
CPU Count: {cpu_count}
pyperf version: {pyperf_version}
python version: {python_version}
""".format(
    platform=suite_metadata["platform"],
    pyperf_version=suite_metadata["perf_version"],
    cpu_count=suite_metadata["cpu_count"],
    python_version=suite_metadata["python_implementation"]
    + suite_metadata["python_version"],
)

print(output)
