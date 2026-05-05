# Nama : Evan Galang Wiryanto
# NIM  : 3337250146
# Kelas: A
# Mata Kuliah: Struktur Data

def find_max(arr):
    if not arr:
        return None, 0
    max_val = arr[0]
    comp_count = 0
    assign_count = 0
    for i in range(1, len(arr)):
        comp_count += 1
        if arr[i] > max_val:
            max_val = arr[i]
            assign_count += 1
    return max_val, comp_count, assign_count

def main():
    data_acak = [23, 45, 12, 67, 89, 34, 56, 78]
    data_menurun = [100, 90, 80, 70, 60]
    data_menaik = [10, 20, 30, 40, 50]
    
    datasets = [ ("Acak", data_acak), ("Menurun", data_menurun), ("Menaik", data_menaik) ]
    for nama, data in datasets:
        maks, comp, assign = find_max(data)
        print(f"{nama}: {data}")
        print(f"Maks: {maks}, Perbandingan: {comp}, Penugasan: {assign}\n")
        
if __name__ == "__main__": main()