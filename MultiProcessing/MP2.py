import concurrent.futures
import time

start = time.perf_counter()
# seconds = 1.5


def do_something(second):
    # second = seconds
    print(f'Sleeping {second} seconds')
    time.sleep(second)
    return f'Done Sleeping in {second}'


with concurrent.futures.ProcessPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    results = [executor.submit(do_something, sec) for sec in secs]

    for f in concurrent.futures.as_completed(results):
        print(f.result())

# process = []
# for _ in range(10):
#     p = mp.Process(target=do_something, args=[seconds])
#     p.start()
#     process.append(p)
#
# for pro in process:
#     pro.join()
#
finish = time.perf_counter()
print(f'Finished in {round(finish - start, 2)} Second(s)')
