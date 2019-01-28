import gevent


def foo():
    print('Running in foo')
    gevent.sleep(0)
    print('Switch to foo again')


def bar():
    print('Running in bar')
    gevent.sleep(0)
    print('Switch to bar again')

gevent.joinall(
    [gevent.spawn(foo),
     gevent.spawn(bar)]
)