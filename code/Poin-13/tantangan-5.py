# Nama : Evan Galang Wiryanto
# NIM : 3337250146
# Kelas : A
# Mata Kuliah : Struktur Data

print("=" * 60)
print("Tantangan 5: Analisis Rekursi dan Memoization (Level: Sulit)")
print("=" * 60)

import time
 
call_count = 0
 
def fib_naif(n):
    global call_count
    call_count += 1
    if n <= 1:
        return n
    return fib_naif(n - 1) + fib_naif(n - 2)
 
memo_cache = {}
 
def fib_memo(n):
    if n in memo_cache:
        return memo_cache[n]
    if n <= 1:
        return n
    memo_cache[n] = fib_memo(n - 1) + fib_memo(n - 2)
    return memo_cache[n]
 
def fib_iter(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

print("\n" + "-" * 80)
print(f"{'n':>5} | {'Hasil':>13} | {'Panggilan Naif':>15} | "
      f"{'Waktu Naif':>11} | {'Waktu Memo':>11} | {'Waktu Iter':>11}")
print("-" * 80)
 
for n_fib in [10, 20, 30, 40]:
    call_count = 0
    memo_cache = {}
 
    t1 = time.perf_counter()
    hasil = fib_naif(n_fib)
    t1 = time.perf_counter() - t1
    panggilan = call_count
 
    memo_cache = {}
    t2 = time.perf_counter()
    fib_memo(n_fib)
    t2 = time.perf_counter() - t2
 
    t3 = time.perf_counter()
    fib_iter(n_fib)
    t3 = time.perf_counter() - t3
 
    print(f"{n_fib:>5} | {hasil:>13,} | {panggilan:>15,} | "
          f"{t1:>11.6f} | {t2:>11.6f} | {t3:>11.6f}")