# Nama : Evan Galang Wiryanto
# NIM  : 3337250146
# Kelas: A
# Mata Kuliah: Struktur Data

print("=" * 65)
print("Tantangan 2: Analisis Algoritma Sorting Sederhana (Level: Sedang)")
print("=" * 65)

import time
import random
import matplotlib.pyplot as plt

def bubble_sort(arr):
    a = arr[:]
    n = len(a)
    comp = swaps = 0
    for i in range(n - 1):
        for j in range(n - i - 1):
            comp += 1
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swaps += 1
    return comp, swaps

def selection_sort(arr):
    a = arr[:]
    n = len(a)
    comp = swaps = 0
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            comp += 1
            if a[j] < a[min_idx]:
                min_idx = j
        if min_idx != i:
            a[i], a[min_idx] = a[min_idx], a[i]
            swaps += 1
    return comp, swaps

def insertion_sort(arr):
    a = arr[:]
    n = len(a)
    comp = shifts = 0
    for i in range(1, n):
        key = a[i]
        j = i - 1
        while j >= 0:
            comp += 1
            if a[j] > key:
                a[j + 1] = a[j]
                shifts += 1
                j -= 1
            else:
                break
        a[j + 1] = key
    return comp, shifts

sizes = [100, 500, 1000, 5000]
data_types = ['acak', 'menaik', 'menurun']

results = {algo: {dt: {'waktu': [], 'comp': [], 'swap': []} for dt in data_types}
           for algo in ['Bubble', 'Selection', 'Insertion']}

print("\n" + "=" * 100)
print("TABEL PERBANDINGAN ALGORITMA SORTING")
print("=" * 100)

for n in sizes:
    data_acak    = [random.randint(1, 10000) for _ in range(n)]
    data_menaik  = list(range(1, n + 1))
    data_menurun = list(range(n, 0, -1))

    for algo_name, sort_func in [('Bubble', bubble_sort),
                                 ('Selection', selection_sort),
                                 ('Insertion', insertion_sort)]:
        for data_name, data in [('acak', data_acak),
                                ('menaik', data_menaik),
                                ('menurun', data_menurun)]:
            start = time.perf_counter()
            cmp, swp = sort_func(data)
            elapsed = time.perf_counter() - start

            # Simpan hasil
            results[algo_name][data_name]['waktu'].append(elapsed)
            results[algo_name][data_name]['comp'].append(cmp)
            results[algo_name][data_name]['swap'].append(swp)

            if n == sizes[0]:   
                pass

            print(f"{algo_name:12} | n={n:5} | {data_name:8} | "
                  f"waktu={elapsed:.6f}s | comp={cmp:8,} | swap={swp:6,}")

plt.figure(figsize=(10, 6))
for algo in ['Bubble', 'Selection', 'Insertion']:
    plt.plot(sizes, results[algo]['acak']['waktu'],
             marker='o', linewidth=2, markersize=8, label=algo)

plt.xlabel('Ukuran Data (n)')
plt.ylabel('Waktu (detik)')
plt.title('Pertumbuhan Waktu pada Data Acak (Average Case)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()
plt.savefig('sorting_acak_waktu.png', dpi=150)
plt.show()

n_idx = sizes.index(1000)   
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

for ax, (data_label, data_key) in zip(axes, [('Data Acak','acak'),
                                              ('Data Menaik (Best)','menaik'),
                                              ('Data Menurun (Worst)','menurun')]):
    algos = ['Bubble', 'Selection', 'Insertion']
    comp_vals = [results[a][data_key]['comp'][n_idx] for a in algos]
    swap_vals = [results[a][data_key]['swap'][n_idx] for a in algos]

    x = range(len(algos))
    width = 0.35
    ax.bar([i - width/2 for i in x], comp_vals, width, label='Perbandingan', color='steelblue')
    ax.bar([i + width/2 for i in x], swap_vals, width, label='Pertukaran/Shift', color='salmon')
    ax.set_xticks(x)
    ax.set_xticklabels(algos)
    ax.set_title(f'Operasi pada n=1000 - {data_label}')
    ax.legend()
    ax.grid(axis='y', linestyle='--', alpha=0.5)

plt.tight_layout()
plt.savefig('sorting_operasi_1000.png', dpi=150)
plt.show()