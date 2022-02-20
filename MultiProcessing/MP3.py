import concurrent.futures
import time
import os

print(os.cpu_count())

start = time.perf_counter()


# seconds = 1.5


def do_something(second):
    # second = seconds
    print(f'Sleeping {second} seconds')
    time.sleep(second)
    return f'Done Sleeping in {second}'


secs = [5, 4, 3, 2, 1]

# with concurrent.futures.ProcessPoolExecutor() as executor:
with concurrent.futures.ThreadPoolExecutor() as executor:
    results = executor.map(do_something, secs)

    # for result in results:
    #     print(result)
# multi-threading is for I/O bound process
# multi-processing is for CPU bound process

finish = time.perf_counter()
print(f'Finished in {round(finish - start, 2)} Second(s)')
