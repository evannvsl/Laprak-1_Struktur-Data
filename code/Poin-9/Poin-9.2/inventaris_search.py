# Nama : Evan Galang Wiryanto
# NIM  : 3337250146
# Kelas : A
# Mata Kuliah : Struktur Data

print("=" * 65)
print("Studi Kasus: Sistem Pencarian Inventaris Toko Elektronik")
print("=" * 65)

import time
import random
import matplotlib.pyplot as plt

Kategori = ["Elektronik", "Aksesoris", "Penyimpanan", "Lainnya"]
Nama_Produk = [
    "Laptop", "Mouse", "Keyboard", "Monitor", "SSD", "RAM",
    "GPU", "Headset", "Webcam", "Speaker", "HDD", "Flash Disk",
    "Router", "UPS", "Power Bank", "Printer", "Scanner", "Joystick"
]

def generate_products(n):
    """Membangkitkan n produk dengan ID format P001, P002, ..."""
    products = []
    for i in range(1, n + 1):
        products.append({
            "id": f"P{i:03d}",
            "nama": f"{random.choice(Nama_Produk)} {random.randint(1, 99)}",
            "kategori": random.choice(Kategori),
            "harga": random.randint(10_000, 20_000_000),
            "terjual": random.randint(0, 1000)
        })
    return products

def cari_produk_id(products, target_id):
    """Pencarian berdasarkan ID (linear)."""
    for p in products:
        if p["id"] == target_id:
            return p
    return None

def cari_produk_nama(products, keyword):
    """Pencarian berdasarkan nama (substring, case insensitive)."""
    kw = keyword.lower()
    return [p for p in products if kw in p["nama"].lower()]

def ukur_waktu(func, *args):
    """Mengembalikan waktu eksekusi (detik)."""
    start = time.perf_counter()
    func(*args)
    return time.perf_counter() - start

ukuran_list = [100, 500, 1000, 5000]
keyword = "Laptop"

waktu_id_awal, waktu_id_tengah, waktu_id_akhir, waktu_id_tidak = [], [], [], []
waktu_nama = []

print("\nPencarian Berdasarkan ID")
print("-" * 70)
print(f"{'Ukuran':>6} | {'ID Awal (s)':>11} | {'ID Tengah (s)':>12} | {'ID Akhir (s)':>11} | {'ID Tidak Ada (s)':>14}")
print("-" * 70)

for n in ukuran_list:
    products = generate_products(n)

    id_awal = "P001"
    id_tengah = f"P{n//2:03d}"
    id_akhir = f"P{n:03d}"
    id_tidak_ada = "P9999"

    t1 = ukur_waktu(cari_produk_id, products, id_awal)
    t2 = ukur_waktu(cari_produk_id, products, id_tengah)
    t3 = ukur_waktu(cari_produk_id, products, id_akhir)
    t4 = ukur_waktu(cari_produk_id, products, id_tidak_ada)

    waktu_id_awal.append(t1 * 1000)
    waktu_id_tengah.append(t2 * 1000)
    waktu_id_akhir.append(t3 * 1000)
    waktu_id_tidak.append(t4 * 1000)

    print(f"{n:>6} | {t1:>11.6f} | {t2:>12.6f} | {t3:>11.6f} | {t4:>14.6f}")

print("\nPencarian Berdasarkan Nama (substring)")
print("-" * 20)
print(f"{'Ukuran':>6} | {'Waktu (s)':>10}")
print("-" * 20)

for n in ukuran_list:
    products = generate_products(n)
    t = ukur_waktu(cari_produk_nama, products, keyword)
    waktu_nama.append(t * 1000)
    print(f"{n:>6} | {t:>10.6f}")

# Grafik 1: Pencarian ID (berbagai skenario)
plt.figure(figsize=(8, 5))
plt.plot(ukuran_list, waktu_id_awal, 'g-o', label='ID Awal (best)')
plt.plot(ukuran_list, waktu_id_tengah, 'b-s', label='ID Tengah')
plt.plot(ukuran_list, waktu_id_akhir, 'r-^', label='ID Akhir (worst)')
plt.plot(ukuran_list, waktu_id_tidak, 'm-D', label='ID Tidak Ada')
plt.xlabel('Ukuran Data (n)')
plt.ylabel('Waktu (ms)')
plt.title('Pencarian ID – Linear Search (berbagai skenario)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('grafik_pencarian_id.png', dpi=150)
plt.show()

# Grafik 2: ID (worst) vs Nama
plt.figure(figsize=(8, 5))
plt.plot(ukuran_list, waktu_id_tidak, 'r-o', label='ID Tidak Ada (worst)')
plt.plot(ukuran_list, waktu_nama, 'b-s', label='Nama (substring)')
plt.xlabel('Ukuran Data (n)')
plt.ylabel('Waktu (ms)')
plt.title('Perbandingan Pencarian ID vs Nama')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('grafik_id_vs_nama.png', dpi=150)
plt.show()