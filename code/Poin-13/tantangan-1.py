# Nama : Evan Galang Wiryanto
# NIM  : 3337250146
# Kelas: A
# Mata Kuliah: Struktur Data

print("=" * 65)
print("Tantangan 1: Implementasi Binary Search (Level: Mudah)")
print("=" * 65)

import matplotlib.pyplot as plt

def linear_search_count(arr, x):
    count = 0
    for i in range(len(arr)):
        count += 1
        if arr[i] == x:
            return i, count
    return -1, count

def binary_search(arr, x):
    low, high = 0, len(arr) - 1
    count = 0
    while low <= high:
        count += 1
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid, count
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1, count

ukuran = [1000, 10000, 100000, 1000000]
lin_steps_list = []
bin_steps_list = []

print(f"{'Ukuran (n)':>12} | {'Langkah Linear':>15} | {'Langkah Binary':>15}")
print("-" * 50)

for n in ukuran:
    data = list(range(1, n + 1))
    target = data[-1]

    _, lin_steps = linear_search_count(data, target)
    _, bin_steps = binary_search(data, target)

    lin_steps_list.append(lin_steps)
    bin_steps_list.append(bin_steps)

    print(f"{n:>12} | {lin_steps:>15,} | {bin_steps:>15}")

# Grafik
plt.figure(figsize=(8,5))
plt.loglog(ukuran, lin_steps_list, 'b-o', linewidth=2, markersize=8, label='Linear Search (O(n))')
plt.loglog(ukuran, bin_steps_list, 'r-s', linewidth=2, markersize=8, label='Binary Search (O(log n))')
plt.xlabel('Ukuran Data (n)')
plt.ylabel('Jumlah Langkah (perbandingan)')
plt.title('Perbandingan Jumlah Langkah: Linear vs Binary Search (skala log-log)')
plt.grid(True, which='both', linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()
plt.savefig('grafik_binary_vs_linear.png', dpi=150)
plt.show()