# Nama : Evan Galang Wiryanto
# NIM  : 3337250146
# Kelas: A
# Mata Kuliah: Struktur Data

import time
import random
import matplotlib.pyplot as plt

print("\n--- TABEL 1.4: Hasil Eksperimen Waktu Linear Search ---")
print("(Poin 9, mengacu Poin 10.1)\n")

def linear_search_plain(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

sizes = [1000, 5000, 10000, 50000, 100000]
waktu_list = []
baseline = None

print(f"{'Ukuran (n)':>12} | {'Waktu (detik)':>15} | {'Rasio':>10} | {'Catatan':>20}")
print("-" * 65)

for n in sizes:
    total = 0
    for _ in range(5):                     # rata‑rata 5 kali
        data = [random.randint(1, 1_000_000) for _ in range(n)]
        target = data[-1]                  # worst case
        start = time.perf_counter()
        linear_search_plain(data, target)
        total += time.perf_counter() - start
    avg = total / 5
    waktu_list.append(avg)

    if baseline is None:
        baseline = avg
        rasio_str = "1.00x"
        catatan = "Baseline"
    else:
        rasio = avg / baseline
        rasio_str = f"{rasio:.2f}x"
        teori = n / 1000
        catatan = "Linear" if abs(rasio - teori) < teori * 0.2 else "Ada overhead"

    print(f"{n:>12} | {avg:>15.6f} | {rasio_str:>10} | {catatan:>20}")

# ====================== GRAFIK ======================
plt.figure(figsize=(8, 5))
plt.plot(sizes, waktu_list, marker='o', linestyle='-', color='blue',
         linewidth=2, markersize=8, label='Linear Search')

# Label dan judul
plt.xlabel('Ukuran Data (n)')
plt.ylabel('Waktu (detik)')
plt.title('Grafik Pertumbuhan Waktu Linear Search')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()

# Tambahkan angka pada setiap titik
for x, y in zip(sizes, waktu_list):
    plt.text(x, y, f'{y:.6f}', ha='center', va='bottom')

plt.tight_layout()
plt.savefig('grafik_tabel14.png', dpi=150)
plt.show()