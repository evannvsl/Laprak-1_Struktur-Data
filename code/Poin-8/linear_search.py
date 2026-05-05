# Nama : Evan Galang Wiryanto
# NIM  : 3337250146
# Kelas: A
# Mata Kuliah: Struktur Data

def linear_search(arr, target):
    for index in range(len(arr)):
        if arr[index] == target:
            return index
    return -1

def main():
    data = [23, 45, 12, 67, 89, 34, 56, 78]
    print("data:", data)
    cari = 67
    hasil = linear_search(data, cari)
    if hasil != -1:
        print(f"Data {cari} ditemukan pada indeks {hasil}.")
    else:
        print(f"Data {cari} tidak ditemukan dalam array.")
        
if __name__ == "__main__":  main()