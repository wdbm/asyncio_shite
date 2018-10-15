import asyncio
import math
import random
import time

import asyncio

def pi_MC(iterations = 100000000):
    count = 0
    for i in range(iterations):
        if random.random() ** 2.0 + random.random() ** 2 <= 1.0:
            count += 1
    pi_estimation = 4.0 * count / iterations
    return pi_estimation

@asyncio.coroutine
def pi_MC_coroutine(iterations = 10000000):
    count = 0
    for i in range(int(iterations)):
        if random.random() ** 2.0 + random.random() ** 2 <= 1.0:
            count += 1
    pi_estimation = 4.0 * count / iterations
    return pi_estimation

def pi_MC_serial(iterations = 100000000):
    print("\nserial estimation of π")
    start_time = time.time()
    pi_estimation = pi_MC(iterations)
    stop_time = time.time()
    print(f"π estimation:    {pi_estimation}")
    print(f"processing time: {stop_time - start_time} s\n")
    return pi_estimation

def pi_MC_asyncio(iterations = 100000000):
    print("\nasyncio estimation of π")
    start_time = time.time()
    loop = asyncio.get_event_loop()
    tasks = [
        pi_MC_coroutine(iterations / 4),
        pi_MC_coroutine(iterations / 4),
        pi_MC_coroutine(iterations / 4),
        pi_MC_coroutine(iterations / 4)
    ]
    pi_estimation = sum(loop.run_until_complete(asyncio.gather(*tasks))) / 4
    loop.close()
    stop_time = time.time()
    print(f"π estimation:    {pi_estimation}")
    print(f"processing time: {stop_time - start_time} s\n")
    return pi_estimation

pi_MC_serial()
pi_MC_asyncio()
