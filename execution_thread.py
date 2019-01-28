import time
import gevent
from gevent import select

start = time.time()
tic = lambda: f'at {time.time()-start:.3} seconds'


def gr1():
    print(f'Started Polling: {tic()}')
    select.select([], [], [], 2)
    print(f'Ended Polling: {tic()}')


def gr2():
    print(f'Started Polling: {tic()}')
    select.select([], [], [], 2)
    print(f'Ended Polling: {tic()}')


def gr3():
    print(f'Hey lets do some stuff while the greenlets poll, {tic()}')
    gevent.sleep(1)


gevent.joinall([
    gevent.spawn(gr1),
    gevent.spawn(gr2),
    gevent.spawn(gr3),
])