# Nama : Evan Galang Wiryanto
# NIM : 3337250146
# Kelas : A
# Mata Kuliah : Struktur Data

print("=" * 65)
print("Soal 1: Modifikasi Linear Search untuk Data Duplikat (Skor 20")
print("=" * 65)

def linear_search(arr, target):
    steps = 0
    for index in range(len(arr)):
        steps += 1
        if arr[index] == target:
            return index, steps
    return -1, steps

def main():
    data = [23, 45, 12, 67, 89, 34, 56, 78]
    test_values = [67, 23, 78, 99]
    for val in test_values: 
        idx, steps = linear_search(data, val)
        if idx != -1:
            print(f"nilai {val} ditemukan di indeks {idx} langkah: {steps}")
        else:
            print(f"nilai {val} tidak ditemukan langkah: {steps}")
    print("data:", data)
    print("-" * 10)
    cari = 23
    idx, steps = linear_search(data, cari)
    if idx != -1:
        print(f"nilai {cari} ditemukan di indeks {idx} langkah: {steps}")
    else:
        print(f"nilai {cari} tidak ditemukan langkah: {steps}")
        
if __name__ == "__main__":  
    main()