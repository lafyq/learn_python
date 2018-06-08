import threading
import asyncio

@asyncio.coroutine
def hello():
    print("hello world!")

    yield from asyncio.sleep(1)
    print("hello python!")


@asyncio.coroutine
def hi():
    print("hi world!")
    print("hi python!")

loop = asyncio.get_event_loop()

tasks = [hello(), hi()]

loop.run_until_complete(asyncio.wait(tasks))

loop.close()