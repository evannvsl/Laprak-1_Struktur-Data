# Nama : Evan Galang Wiryanto
# NIM  : 3337250146
# Kelas : A
# Mata Kuliah : Struktur Data

print("=" * 60)
print("Studi Kasus 1: E-Commerce Shopfast")
print("=" * 60)

import time
import random
import heapq

Kategori = ["Elektronik", "Aksesoris", "Penyimpanan", "Lainnya"]
Nama_Produk = [
    "Laptop", "Mouse", "Keyboard", "Monitor", "SSD", "RAM",
    "GPU", "Headset", "Webcam", "Speaker", "HDD", "Flash Disk",
    "Router", "UPS", "Power Bank", "Printer", "Scanner", "Joystick"
]

def generate_products(n):
    """Membangkitkan n produk dengan atribut acak."""
    return [
        {
            "id": i + 1,
            "nama": f"{random.choice(Nama_Produk)} {random.randint(1, 99)}",
            "harga": random.randint(10_000, 20_000_000),
            "kategori": random.choice(Kategori),
            "terjual": random.randint(0, 1000)
        }
        for i in range(n)
    ]
    
def cari_produk_nama(products, keyword):
    """Linear search berdasarkan nama (case insensitive)."""
    keyword = keyword.lower()
    return [p for p in products if keyword in p["nama"].lower()]

def cari_produk_termahal(products):
    """Mencari produk dengan harga tertinggi (O(n))."""
    if not products:
        return None
    return max(products, key=lambda p: p["harga"])

def cari_produk_termurah(products):
    """Mencari produk dengan harga terendah (O(n))."""
    if not products:
        return None
    return min(products, key=lambda p: p["harga"])

def top5_selection(products):
    """
    Selection parsial: ulangi 5 kali cari maksimum lalu hapus.
    Kompleksitas: O(5n) ≈ O(n), namun ada overhead hapus.
    """
    hasil = []
    sisa = products.copy()
    for _ in range(5):
        if not sisa:
            break
        maks = max(sisa, key=lambda p: p["harga"])
        hasil.append(maks)
        sisa.remove(maks)
    return hasil

def top5_heap(products):
    """Menggunakan heapq.nlargest (O(n log 5) ≈ O(n))."""
    return heapq.nlargest(5, products, key=lambda p: p["harga"])

def top5_sorting(products):
    """Sorting penuh lalu ambil 5 teratas (O(n log n))."""
    return sorted(products, key=lambda p: p["harga"], reverse=True)[:5]

def ukur_waktu(func, *args):
    """Mengembalikan waktu eksekusi dalam detik."""
    start = time.perf_counter()
    func(*args)
    return time.perf_counter() - start

def main():
    ukuran_list = [100, 500, 1000]
    keyword = "Laptop"

    print("\nTabel Waktu Eksekusi (detik)")
    print("-" * 95)
    print(f"{'n':>7} | {'Cari Nama':>10} | {'Termahal':>9} | {'Termurah':>9} | "
          f"{'Top5 (select)':>14} | {'Top5 (heap)':>13} | {'Top5 (sort)':>12}")
    print("-" * 95)

    for n in ukuran_list:
        products = generate_products(n)

        t_nama    = ukur_waktu(cari_produk_nama, products, keyword)
        t_mahal   = ukur_waktu(cari_produk_termahal, products)
        t_murah   = ukur_waktu(cari_produk_termurah, products)
        t_top5sel = ukur_waktu(top5_selection, products)
        t_top5heap = ukur_waktu(top5_heap, products)
        t_top5sort = ukur_waktu(top5_sorting, products)

        print(f"{n:>7} | {t_nama:>10.6f} | {t_mahal:>9.6f} | {t_murah:>9.6f} | "
              f"{t_top5sel:>14.6f} | {t_top5heap:>13.6f} | {t_top5sort:>12.6f}")

    print("\n" + "-" * 35)
    print("Contoh Hasil pada 1000 Produk ")
    print("-" * 35)
    produk_1k = generate_products(1000)
    termahal = cari_produk_termahal(produk_1k)
    termurah = cari_produk_termurah(produk_1k)
    top5 = top5_heap(produk_1k)  

    print(f"Produk termahal : {termahal['nama']} - Rp{termahal['harga']:,}")
    print(f"Produk termurah : {termurah['nama']} - Rp{termurah['harga']:,}")
    print("Top 5 termahal :")
    for i, p in enumerate(top5, 1):
        print(f"  {i}. {p['nama']} - Rp{p['harga']:,}")

if __name__ == "__main__":
    main()