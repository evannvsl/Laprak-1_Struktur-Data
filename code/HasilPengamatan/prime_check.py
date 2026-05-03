# Nama : Evan Galang Wiryanto
# NIM : 3337250146
# Kelas : A
# Mata Kuliah : Struktur Data

import math
 
def is_prime_iter(n):
    """Cek prima optimasi (loop ganjil hingga √n), hitung iterasi."""
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
 
 
test_numbers_13 = [2, 3, 17, 19, 23, 97, 100, 101, 121, 997, 999, 1000]
 
print(f"{'Bilangan (n)':<10} | {'Prima?':<8} | {'Iterasi':<10} | "
      f"{'√n':<10} | {'Keterangan':>30}")
print("-" * 75)
 
for n in test_numbers_13:
    prima, iterasi = is_prime_iter(n)
    akar = int(math.sqrt(n))
    status = "Ya" if prima else "Tidak"
 
    if n == 2 or n == 3:
        ket = "Base case"
    elif not prima and n % 2 == 0:
        ket = "Habis dibagi 2"
    elif not prima:
        faktor = next((i for i in range(3, n, 2) if n % i == 0), None)
        ket = f"Habis dibagi {faktor}"
    else:
        last_i = 3 + (iterasi - 1) * 2 if iterasi > 0 else 3
        ket = f"Diuji 3,5,...,{last_i}"
 
    print(f"{n:>10} | {status:<8} | {iterasi:<10} | {akar:<10} | {ket:>30}")