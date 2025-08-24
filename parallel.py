from concurrent.futures import ProcessPoolExecutor
import time

# Fibonacci function with tasks
def fib_task(n, depth=0, max_depth=3):
    if n <= 1:
        return n

    # Create tasks only for upper levels of recursion
    if depth < max_depth:
        with ProcessPoolExecutor() as executor:
            f1 = executor.submit(fib_task, n-1, depth+1, max_depth)
            f2 = executor.submit(fib_task, n-2, depth+1, max_depth)
            return f1.result() + f2.result()
    else:
        # Normal recursion (sequential)
        return fib_task(n-1, depth+1, max_depth) + fib_task(n-2, depth+1, max_depth)


if __name__ == "__main__":
    n = int(input("Enter n for Fibonacci: "))

    # Sequential version
    def fib_seq(n):
        if n <= 1:
            return n
        return fib_seq(n-1) + fib_seq(n-2)

    start = time.time()
    result_seq = fib_seq(n)
    end = time.time()
    print(f"\nSequential Fibonacci({n}) = {result_seq}")
    print("Execution Time (Sequential):", round(end - start, 4), "seconds")

    # Parallel (tasks) version
    start = time.time()
    result_par = fib_task(n)
    end = time.time()
    print(f"\nParallel Fibonacci({n}) = {result_par}")
    print("Execution Time (Tasks/Parallel):", round(end - start, 4), "seconds")