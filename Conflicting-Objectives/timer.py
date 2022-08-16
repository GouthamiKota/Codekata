from contextlib import contextmanager
from time import time


@contextmanager
def timing():
    start = time()
    try:
        yield
    finally:
        print(f'Took: {time() - start} seconds')
