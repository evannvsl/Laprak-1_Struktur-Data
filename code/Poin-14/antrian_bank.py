# Nama : Evan Galang Wiryanto
# NIM  : 3337250146
# Kelas : A
# Mata Kuliah : Struktur Data

print("=" * 60)
print("Studi Kasus 2: Sistem Antrian Bank")
print("=" * 60)

import time
import random
from collections import deque

Jumlah_Nasabah = 1000
Batas_Datang = (1, 3)      
Batas_Layanan = (3, 10)    
Jumlah_Uji = 10000         
Uji_Operasi = 1000       

def simulasi_antrian(jumlah):
    """Simulasi antrian FIFO dengan deque. Mengembalikan riwayat dan rata‑rata tunggu."""
    antrian = deque()
    riwayat = []

    # nasabah
    for i in range(1, jumlah + 1):
        waktu_datang = i * random.randint(*Batas_Datang)
        lama_layanan = random.randint(*Batas_Layanan)
        antrian.append({
            "nomor": i,
            "nama": f"Nasabah-{i:04d}",
            "waktu_datang": waktu_datang,
            "lama_layanan": lama_layanan
        })

    # fifo
    waktu_selesai = 0
    total_tunggu = 0
    while antrian:
        nasabah = antrian.popleft()
        mulai = max(waktu_selesai, nasabah["waktu_datang"])
        nasabah["waktu_tunggu"] = mulai - nasabah["waktu_datang"]
        waktu_selesai = mulai + nasabah["lama_layanan"]
        total_tunggu += nasabah["waktu_tunggu"]
        riwayat.append(nasabah)

    return riwayat, total_tunggu / jumlah

def cari_nomor_antrian(riwayat, nomor):
    """Linear search berdasarkan nomor antrian."""
    for n in riwayat:
        if n["nomor"] == nomor:
            return n
    return None

def uji_perbandingan(besar, ulangi):
    """Membandingkan deque.popleft() vs list.pop(0)."""
    dq = deque(range(besar))
    start = time.perf_counter()
    for _ in range(ulangi):
        dq.popleft()
        dq.append(0)
    t_deque = time.perf_counter() - start

    lst = list(range(besar))
    start = time.perf_counter()
    for _ in range(ulangi):
        lst.pop(0)
        lst.append(0)
    t_list = time.perf_counter() - start

    return t_deque, t_list

def main():
    print("\n === Simulasi 1000 Nasabah ===")
    riwayat, rata = simulasi_antrian(Jumlah_Nasabah)
    print(f"Rata‑rata waktu tunggu : {rata:.2f} menit")

    print("\n=== Pencarian Nasabah (Linear Search) ===")
    for case, nomor in [("Best (pertama)", riwayat[0]["nomor"]),
                         ("Worst (terakhir)", riwayat[-1]["nomor"]),
                         ("Tidak ditemukan", 99999)]:
        start = time.perf_counter()
        cari_nomor_antrian(riwayat, nomor)
        print(f"  {case:20s} : {time.perf_counter()-start:.6f} detik")

    print("\n=== Perbandingan Deque vs List ===")
    t_dq, t_ls = uji_perbandingan(Jumlah_Uji, Uji_Operasi)
    print(f"  deque.popleft() + append  : {t_dq:.6f} detik  (O(1))")
    print(f"  list.pop(0) + append      : {t_ls:.6f} detik  (O(n))")
    print(f"  deque lebih cepat         : {t_ls/t_dq:.1f}x")

if __name__ == "__main__":
    main()
    
    # Analisis
    print("""
  =========================================================================
    ANALISIS KOMPLEKSITAS
  =========================================================================
    1. Antrian FIFO dengan deque
       - append() dan popleft() : O(1) → sangat cocok untuk antrian.

    2. Pencarian nomor antrian (linear search)
       - Best case   : O(1)   → ditemukan di awal.
       - Worst case  : O(n)   → di akhir / tidak ditemukan.
       - Average case: O(n/2) ≈ O(n).

    3. Rata‑rata waktu tunggu
       - Satu pass seluruh riwayat → O(n).

    4. list.pop(0) vs deque.popleft()
       - list.pop(0) menggeser seluruh elemen → O(n).
       - deque.popleft() hanya mengubah dua pointer → O(1).
       - Terbukti deque JAUH lebih cepat (puluhan hingga ratusan kali).

  =========================================================================
    REKOMENDASI
  =========================================================================
    - Gunakan deque untuk semua operasi antrian (FIFO/LIFO).
    - Untuk pencarian nomor antrian yang berulang kali, ganti
      linear search dengan dictionary (nomor → nasabah) → O(1).
    - Jika data nasabah sangat besar, gunakan database berindeks.
  """)

