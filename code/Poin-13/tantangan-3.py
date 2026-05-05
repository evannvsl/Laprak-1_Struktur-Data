# Nama : Evan Galang Wiryanto
# NIM : 3337250146
# Kelas : A
# Mata Kuliah : Struktur Data

print("=" * 75)
print("Tantangan 3: Visualisasi Pertumbuhan Waktu dengan Matplotlib (Level: Sedang)")
print("=" * 75)

import matplotlib.pyplot as plt

n = [1000, 5000, 10000, 50000, 100000]

waktu_linear = [0.000123, 0.000567, 0.001234, 0.005678, 0.011234]
waktu_binary = [0.0000012, 0.0000013, 0.0000014, 0.0000015, 0.0000016]
waktu_bubble = [0.004,    0.082,    0.312,    8.12,     35.21]

plt.figure(figsize=(8, 5))
plt.loglog(n, waktu_linear, 'b-o', linewidth=2, markersize=8, label='Linear Search')
plt.loglog(n, waktu_binary, 'r-s', linewidth=2, markersize=8, label='Binary Search')
plt.loglog(n, waktu_bubble, 'g-^', linewidth=2, markersize=8, label='Bubble Sort')

plt.xlabel('Ukuran Data (n)')
plt.ylabel('Waktu (detik)')
plt.title('Perbandingan Waktu Eksekusi (Skala Log-Log)')
plt.legend()
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# Simpan grafik
plt.savefig('grafik_perbandingan.png', dpi=150)
plt.show()