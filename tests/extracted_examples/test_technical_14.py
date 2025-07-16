"""
Extracted from /home/kevin/Projects/Common-Questions/content/interview-questions/technical.md
"""

import threading
import multiprocessing
import time

# Threading example
def worker_thread(name):
    for i in range(5):
        print(f"Thread {name}: {i}")
        time.sleep(1)

# Create and start threads
threads = []
for i in range(3):
    t = threading.Thread(target=worker_thread, args=(f"T{i}",))
    threads.append(t)
    t.start()

# Wait for all threads to complete
for t in threads:
    t.join()

# Multiprocessing example
def worker_process(name):
    for i in range(5):
        print(f"Process {name}: {i}")
        time.sleep(1)

# Create and start processes
processes = []
for i in range(3):
    p = multiprocessing.Process(target=worker_process, args=(f"P{i}",))
    processes.append(p)
    p.start()

# Wait for all processes to complete
for p in processes:
    p.join()

# Test function
def test_syntax():
    """Test that code compiles without syntax errors."""
    pass
