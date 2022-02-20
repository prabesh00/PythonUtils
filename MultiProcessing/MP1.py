import multiprocessing as mp
import time

start = time.perf_counter()
seconds = 1.5


def do_something(second):
    # second = seconds
    print(f'Sleeping {second} seconds')
    time.sleep(second)
    print('Done Sleeping')


process = []
for _ in range(10):
    p = mp.Process(target=do_something, args=[seconds])
    p.start()
    process.append(p)

for pro in process:
    pro.join()

finish = time.perf_counter()
print(f'Finished in {round(finish - start, 2)} Second(s)')
