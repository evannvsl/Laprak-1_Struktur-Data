# Nama : Evan Galang Wiryanto
# NIM  : 3337250146
# Kelas: A
# Mata Kuliah: Struktur Data

import time

print("=" * 65)
print("Soal 3: Perbandingan Algoritma Prima Naif vs Optimasi (Skor 25)")
print("=" * 65)

def is_prime_naif(n):
    if n <= 1:
        return False, 0
    count = 0
    for i in range(2, n):       
        count += 1
        if n % i == 0:
            return False, count
    return True, count

def is_prime_optimasi(n):
    if n <= 1:
        return False, 0
    if n == 2:
        return True, 0
    if n % 2 == 0:
        return False, 0
    count = 0
    i = 3
    while i * i <= n:
        count += 1
        if n % i == 0:
            return False, count
        i += 2
    return True, count

test_numbers = [997, 1000, 1000003, 10000000]

print("\n" + "-" * 90)
print(f"{'Bilangan':>10} | {'Prima?':>6} | {'Iter Naif':>9} | {'Iter Opt':>8} | "
      f"{'Waktu Naif(s)':>13} | {'Waktu Opt(s)':>13} | {'Percepatan':>10}")
print("-" * 90)

total_percepatan = 0
jumlah_uji = len(test_numbers)

for n in test_numbers:
    start = time.perf_counter()
    prima_naif, iter_naif = is_prime_naif(n)
    waktu_naif = time.perf_counter() - start

    start = time.perf_counter()
    prima_opt, iter_opt = is_prime_optimasi(n)
    waktu_opt = time.perf_counter() - start

    if waktu_opt > 0:
        percepatan = waktu_naif / waktu_opt
    else:
        percepatan = float('inf')

    total_percepatan += percepatan

    status = "Ya" if prima_opt else "Tidak"

    print(f"{n:>10} | {status:>6} | {iter_naif:>9,} | {iter_opt:>8} | "
          f"{waktu_naif:>13.6f} | {waktu_opt:>13.6f} | {percepatan:>9.1f}x")