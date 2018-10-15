import asyncio

@asyncio.coroutine
def function_a():
    print("running function a")
    return 1

@asyncio.coroutine
def function_b():
    print("running function b")
    return 2

loop = asyncio.get_event_loop()
tasks = [
    function_a(),
    function_b()
]
a, b = loop.run_until_complete(asyncio.gather(*tasks))
print(a + b)
loop.close()
