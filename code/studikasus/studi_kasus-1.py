# Nama : Evan Galang Wiryanto
# NIM : 3337250146
# Kelas : A
# Mata Kuliah : Struktur Data

import time
import random
import heapq

KATEGORI = ["Elektronik", "Aksesoris", "Penyimpanan", "Lainnya"]
NAMA_PRODUK = [
    "Laptop", "Mouse", "Keyboard", "Monitor", "SSD", "RAM",
    "GPU", "Headset", "Webcam", "Speaker", "HDD", "Flash Disk",
    "Router", "UPS", "Power Bank", "Printer", "Scanner", "Joystick"
]

def generate_products(n):
    """Membangkitkan n produk dengan atribut acak."""
    return [
        {
            "id": i + 1,
            "nama": f"{random.choice(NAMA_PRODUK)} {random.randint(1, 99)}",
            "harga": random.randint(10_000, 20_000_000),
            "kategori": random.choice(KATEGORI),
            "terjual": random.randint(0, 1000)
        }
        for i in range(n)
    ]

def cari_produk_nama(products, keyword):
    """Pencarian produk berdasarkan nama (case insensitive, linear search)."""
    keyword_lower = keyword.lower()
    return [p for p in products if keyword_lower in p["nama"].lower()]

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
    Mengambil 5 produk termahal dengan selection parsial (tanpa sorting penuh).
    Kompleksitas: O(n * 5) ≈ O(n).
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
    """Mengambil 5 produk termahal menggunakan heapq (O(n log 5) ≈ O(n))."""
    return heapq.nlargest(5, products, key=lambda p: p["harga"])

def top5_sorting(products):
    """Mengambil 5 produk termahal dengan sorting penuh (O(n log n))."""
    return sorted(products, key=lambda p: p["harga"], reverse=True)[:5]

def ukur_waktu(func, *args, **kwargs):
    """Mengembalikan waktu eksekusi fungsi dalam detik."""
    start = time.perf_counter()
    func(*args, **kwargs)
    return time.perf_counter() - start

def main():
    print("  STUDI KASUS 1: E-COMMERCE SHOPFAST")

    ukuran_list = [100, 500, 1000]
    keyword = "Laptop"

    print(f"\n{'Ukuran':>7} | {'Cari Nama':>11} | {'Termahal':>10} | "
          f"{'Termurah':>10} | {'Top5 (select)':>14} | {'Top5 (heap)':>12} | {'Top5 (sort)':>12}")
    print("-" * 85)

    for n in ukuran_list:
        products = generate_products(n)

        t_nama    = ukur_waktu(cari_produk_nama, products, keyword)
        t_mahal   = ukur_waktu(cari_produk_termahal, products)
        t_murah   = ukur_waktu(cari_produk_termurah, products)
        t_top5sel = ukur_waktu(top5_selection, products)
        t_top5heap = ukur_waktu(top5_heap, products)
        t_top5sort = ukur_waktu(top5_sorting, products)

        print(f"{n:>7} | {t_nama:>11.6f} | {t_mahal:>10.6f} | "
              f"{t_murah:>10.6f} | {t_top5sel:>14.6f} | {t_top5heap:>12.6f} | {t_top5sort:>12.6f}")

    print("\n" + "=" * 70)
    print("  Contoh hasil untuk 1.000 produk:")
    print("=" * 70)
    produk_1k = generate_products(1000)

    termahal = cari_produk_termahal(produk_1k)
    termurah = cari_produk_termurah(produk_1k)
    top5_sel = top5_selection(produk_1k)

    print(f"  Produk termahal : {termahal['nama']} - Rp{termahal['harga']:,}")
    print(f"  Produk termurah : {termurah['nama']} - Rp{termurah['harga']:,}")
    print(f"  Top 5 termahal  :")
    for i, p in enumerate(top5_sel, 1):
        print(f"    {i}. {p['nama']} - Rp{p['harga']:,}")

    # =========================================================================
    # ANALISIS & REKOMENDASI
    # =========================================================================
    print("\n" + "=" * 70)
    print("  ANALISIS & REKOMENDASI")
    print("=" * 70)
    print("""
1. Waktu pencarian produk termahal di 1000 data:
   - Metode linear O(n) memakan waktu < 0.001 detik, sangat cepat.
   - Untuk jutaan data, metode ini akan tetap O(n) dan mungkin terasa lambat.

2. Efisiensi metode Top 5:
   - Selection parsial (O(n*5)) secara praktis lebih cepat daripada sorting
     penuh (O(n log n)) untuk n kecil. Namun di Python, Timsort sangat
     dioptimalkan sehingga sorting penuh seringkali lebih cepat pada data < 10rb.
   - Penggunaan heapq.nlargest() (O(n log k)) adalah yang paling seimbang
     dan direkomendasikan untuk k kecil.

3. Fitur paling lambat:
   - Pencarian nama dengan substring (linear) adalah yang paling lambat
     karena memeriksa setiap elemen DAN melakukan operasi string `in`.
   - Top-5 dengan selection parsial juga memakan waktu lebih banyak daripada
     termahal/termurah karena harus melakukan 5 kali pass.

4. Rekomendasi perbaikan:
   - Gunakan dictionary (hash map) dengan key = id produk untuk pencarian
     berdasarkan ID -> O(1).
   - Untuk pencarian nama, bangun inverted index (kata -> list produk) atau
     gunakan search engine sederhana (mis. Whoosh) agar pencarian substring
     menjadi O(1) rata-rata.
   - Untuk fitur "termahal/termurah" dan "top-k", pertahankan array tetapi
     gunakan heapq untuk efisiensi.
   - Jika data sangat besar dan fitur pencarian kompleks, beralihlah ke
     database (SQLite/PostgreSQL) dengan full‑text search.
""")

if __name__ == "__main__":
    main()