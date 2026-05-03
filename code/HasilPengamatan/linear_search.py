# Nama : Evan Galang Wiryanto
# NIM : 3337250146
# Kelas : A
# Mata Kuliah : Struktur Data

from py_compile import main
 
data_array = [23, 45, 12, 67, 89, 34, 56, 78]
test_values_11 = [67, 23, 78, 99]
 
 
def linear_search_step(arr, x):
    count = 0
    for i in range(len(arr)):
        count += 1
        if arr[i] == x:
            return i, count
    return -1, count
 
 
def label_posisi(idx, n):
    if idx == -1:
        return "Tidak Ada"
    elif idx == 0:
        return "Awal"
    elif idx == n - 1:
        return "Akhir"
    else:
        return "Tengah"
 
 
print(f"Array data: {data_array}   (n = {len(data_array)})")
print()
print(f"{'Nilai Dicari':>13} | {'Ditemukan?':>10} | {'Indeks':>7} | "
      f"{'Jumlah Langkah':>15} | {'Posisi dalam Data':>18}")
print("-" * 72)
 
for val in test_values_11:
    idx, steps = linear_search_step(data_array, val)
    found = "Ya" if idx != -1 else "Tidak"
    posisi = label_posisi(idx, len(data_array))
    print(f"{val:>13} | {found:>10} | {idx:>7} | "
          f"{steps:>15} | {posisi:>18}")
    
if __name__ == "__main__": main()