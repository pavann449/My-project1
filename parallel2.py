import threading

def work(i, thread_id):
    print(f"Thread {thread_id}: Iteration {i}")

if __name__ == "__main__":
    n = int(input("Enter number of iterations: "))

    threads = []
    for i in range(n):
        t = threading.Thread(target=work, args=(i, i))  # thread_id = iteration index
        threads.append(t)
        t.start()

    # Wait for all threads to complete
    for t in threads:
        t.join()
