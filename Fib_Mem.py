import time

m = dict()
def fib_mem(n):
    if n < 2:
        return n
    elif m.get(n) != None:
        return m[n]
    else:
        m[n] = fib_mem(n - 1) + fib_mem(n - 2)
        return m[n]

n = 100
start = time.time()
print(fib_mem(n))
print('Memoization: {} seconds' . format(time.time() - start))
