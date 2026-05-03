# Nama : Evan Galang Wiryanto
# NIM : 3337250146
# Kelas : A
# Mata Kuliah : Struktur Data

import time
import random
 
n_kontak = 10000
nama_list = [f"Nama{i}" for i in range(n_kontak)]
 
kontak_list = [{"nama": n, "telepon": f"08{random.randint(10000000, 99999999)}"}
               for n in nama_list]
 
kontak_dict = {item["nama"]: item["telepon"] for item in kontak_list}
 
nama_uji = random.choices(nama_list, k=1000)
 
def cari_list(data, target):
    for item in data:
        if item["nama"] == target:
            return item["telepon"]
    return None
 
def cari_dict(data, target):
    return data.get(target)
 
t1 = time.perf_counter()
for nama in nama_uji:
    cari_list(kontak_list, nama)
waktu_list = time.perf_counter() - t1
 
t2 = time.perf_counter()
for nama in nama_uji:
    cari_dict(kontak_dict, nama)
waktu_dict = time.perf_counter() - t2
 
print(f"\nJumlah kontak             : {n_kontak:,}")
print(f"Jumlah pencarian          : 1.000")
print(f"Waktu Linear Search       : {waktu_list:.4f} detik  (O(n) per pencarian)")
print(f"Waktu Dictionary Search   : {waktu_dict:.4f} detik  (O(1) per pencarian)")
print(f"Dictionary lebih cepat    : {waktu_list/waktu_dict:.1f}x")