import time
import random
from collections import deque

Jumlah_Nasabah = 1000
Batas_Datang_Min, Batas_Datang_Max = 1, 3   
Layanan_Min, Layanan_Max = 3, 10
Jumlah_Uji_Queue = 10000
Uji_Operasi = 1000

def buat_simulasi_antrian(jumlah):
    """
    Membuat simulasi antrian bank dengan deque.
    Mengembalikan (riwayat_layanan, rata_rata_waktu_tunggu).
    """
    antrian = deque()
    riwayat = []

    for i in range(1, jumlah + 1):
        waktu_datang = i * random.randint(Batas_Datang_Min, Batas_Datang_Max)
        lama_layanan = random.randint(Layanan_Min, Layanan_Max)
        antrian.append({
            "nomor": i,
            "nama": f"Nasabah-{i:04d}",
            "waktu_datang": waktu_datang,
            "lama_layanan": lama_layanan
        })

    waktu_selesai = 0
    total_tunggu = 0
    while antrian:
        nasabah = antrian.popleft()
        mulai_layanan = max(waktu_selesai, nasabah["waktu_datang"])
        waktu_tunggu = mulai_layanan - nasabah["waktu_datang"]
        waktu_selesai = mulai_layanan + nasabah["lama_layanan"]

        nasabah["waktu_tunggu"] = waktu_tunggu
        total_tunggu += waktu_tunggu
        riwayat.append(nasabah)

    rata_tunggu = total_tunggu / jumlah
    return riwayat, rata_tunggu

def cari_nasabah_linear(riwayat, nomor_target):
    """Pencarian nasabah berdasarkan nomor antrian (linear search)."""
    for nasabah in riwayat:
        if nasabah["nomor"] == nomor_target:
            return nasabah
    return None


def ukur_kecepatan_deque_vs_list(besar, ulangi):
    """
    Membandingkan performa deque.popleft() vs list.pop(0) + append.
    Mengembalikan (waktu_deque, waktu_list).
    """
    dq = deque(range(besar))
    start = time.perf_counter()
    for _ in range(ulangi):
        dq.popleft()
        dq.append(0)
    waktu_deque = time.perf_counter() - start

    # list biasa
    lst = list(range(besar))
    start = time.perf_counter()
    for _ in range(ulangi):
        lst.pop(0)
        lst.append(0)
    waktu_list = time.perf_counter() - start

    return waktu_deque, waktu_list

def main():
    riwayat, rata_tunggu = buat_simulasi_antrian(Jumlah_Nasabah)

    print(f"\nSimulasi {Jumlah_Nasabah} nasabah:")
    print(f"Rata-rata waktu tunggu : {rata_tunggu:.2f} menit")

    print("\n=== Pencarian Nasabah ===")
    # Best case
    start = time.perf_counter()
    cari_nasabah_linear(riwayat, riwayat[0]["nomor"])
    t_best = time.perf_counter() - start
    print(f"Best case (nomor pertama)     : {t_best:.6f} detik")

    # Worst case
    start = time.perf_counter()
    cari_nasabah_linear(riwayat, riwayat[-1]["nomor"])
    t_worst = time.perf_counter() - start
    print(f"Worst case (nomor terakhir)   : {t_worst:.6f} detik")

    # Tidak ditemukan
    start = time.perf_counter()
    cari_nasabah_linear(riwayat, 99999)
    t_notfound = time.perf_counter() - start
    print(f"Tidak ditemukan               : {t_notfound:.6f} detik")

    print("\n=== Perbandingan deque vs list ===")
    t_deque, t_list = ukur_kecepatan_deque_vs_list(Jumlah_Uji_Queue, Uji_Operasi)
    print(f"deque.popleft()+append()      : {t_deque:.6f} detik (O(1) per operasi)")
    print(f"list.pop(0)+append()          : {t_list:.6f} detik (O(n) per pop(0))")
    print(f"deque lebih cepat             : {t_list/t_deque:.1f}x")
