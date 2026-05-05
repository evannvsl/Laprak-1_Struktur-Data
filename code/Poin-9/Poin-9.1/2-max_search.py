# Nama : Evan Galang Wiryanto
# NIM : 3337250146
# Kelas : A
# Mata Kuliah : Struktur Data

print("=" * 65)
print("Soal 2: Analisis Best dan Worst Case Pencarian Maksimum (Skor 20)")
print("=" * 65)

def find_max_detail(arr):
    if not arr:
        return None, 0, 0
    maks = arr[0]
    comp = 0
    assign = 0  
    for i in range(1, len(arr)):
        comp += 1
        if arr[i] > maks:
            maks = arr[i]
            assign += 1
    return maks, comp, assign
 
 
datasets_12 = [
    ("Acak",    [23, 45, 12, 67, 89, 34, 56, 78]),
    ("Menurun", [100, 90, 80, 70, 60]),
    ("Menaik",  [10, 20, 30, 40, 50]),
]
print("\n" + "-" * 120)
print(f"{'Jenis Data':>10} | {'Data':>40} | {'Maks':>6} | "
      f"{'Perbandingan':>13} | {'Assignment':>10} | {'Total Langkah':>14}")
print("-" * 120)
 
for nama, data in datasets_12:
    maks, comp, assign = find_max_detail(data)
    print(f"{nama:>10} | {str(data):>40} | {maks:>6} | "
          f"{comp:>13} | {assign:>10} | {comp + assign:>14}")