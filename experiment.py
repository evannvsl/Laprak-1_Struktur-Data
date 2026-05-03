import time
import random

def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

def generate_data(n):
    return [random.randint(1, 1000) for _ in range(n)]

def measure_time(search_func, arr, x):
    start = time.perf_counter()
    search_func(arr, x)
    end = time.perf_counter()
    return end - start

sizes = [1000, 5000, 10000, 50000, 100000]

def main():
    print("=" * 60)
    print("Eksperimen Waktu Linear Search")
    print("=" * 60)
    
    print(f"{'Ukuran(n)':<10} {'Waktu(detik)':<15}")
    print("-" * 60)
    
    for n in sizes:
        data = generate_data(n)
        target = data[-1]
        waktu = measure_time(linear_search, data, target)
        print(f"{n:<15} {waktu:20.6f}")

if __name__ == "__main__":
    main()