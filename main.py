import sys
import time
import functools
import requests
from collections import defaultdict
from heapq import heappush, heappop

def lfu_cache(max_size):
    def decorator(func):
        cache = {}
        frequency = []
        counter = 0

        def wrapper(url, first_n=100):
            nonlocal counter

            if url in cache:
                freq, content = cache[url]
                heappush(frequency, (freq + 1, counter, url))
                counter += 1
                return content

            res = requests.get(url)
            content = res.content[:first_n] if first_n else res.content

            if len(cache) >= max_size:
                while True:
                    freq, _, least_frequent_url = heappop(frequency)
                    if least_frequent_url in cache and cache[least_frequent_url][0] == freq:
                        del cache[least_frequent_url]
                        break

            heappush(frequency, (1, counter, url))
            counter += 1
            cache[url] = (1, content)
            return content

        return wrapper

    return decorator

def size(f):
    def internal(*args, **kwargs):
        size = sys.getsizeof(f(*args, **kwargs))
        result = f(*args, **kwargs)
        print(f'Result of the function {f.__name__} with params {args}, {kwargs}: {result}')
        print (f'size of the result of the function {f.__name__} with params {args}, {kwargs}: {size} bytes')
    return internal

@size
@lfu_cache(max_size=4)
def fetch_url(url, first_n=100):
    """Fetch a given url"""
    res = requests.get(url)
    return res.content[:first_n] if first_n else res.content

fetch_url('https://google.com')
