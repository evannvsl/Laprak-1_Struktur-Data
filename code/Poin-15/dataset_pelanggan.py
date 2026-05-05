# Nama : Evan Galang Wiryanto
# NIM  : 3337250146
# Kelas : A
# Mata Kuliah : Struktur Data

print("=" * 60)
print("Proyek Mini: Analisis Kinerja Algoritma pada Dataset 50.000 Pelanggan")
print("=" * 60)

import time
import random
import csv
from collections import defaultdict, Counter
import heapq
import matplotlib.pyplot as plt

# Tahap 1: Generate Data (10%) =======
Nama_Pelanggan = [
    # Detective Conan
    "Edogawa Conan", "Kudo Shinichi", "Mouri Ran", "Haibara Ai",
    "Hattori Heiji", "Toyama Kazuha", "Suzuki Sonoko", "Kuroba Kaito",
    "Miyano Shiho", "Akai Shuichi", "Amuro Tooru", "Sera Masumi",
    "Megure Juzo", "Takagi Wataru", "Sato Miwako", "Chiba Kazunobu",
    "Yamamura Misao", "Yokomizo Jugo", "Kisaki Eri", "Hakuba Saguru",
    # Hibike! Euphonium
    "Oumae Kumiko", "Kousaka Reina", "Tanaka Asuka", "Nakagawa Natsuki",
    "Yoroizuka Mizore", "Kasashima Nozomi", "Hijiri Kanade",
    "Tsukamoto Shuuichi", "Goto Hazuki", "Kawashima Sapphire",
    "Kato Yuko", "Yoshii Junna",
    # Umineko
    "Ushiromiya Battler", "Ushiromiya Beatrice", "Ushiromiya Ange",
    "Ushiromiya Maria", "Ushiromiya Eva", "Ushiromiya Rudolf",
    "Ushiromiya Kyrie", "Ushiromiya Jessica",
    "Virgilia", "Ronove", "Gaap",
    # Fairy Tail 
    "Natsu Dragneel", "Lucy Heartfilia", "Erza Scarlet", "Gray Fullbuster",
    "Wendy Marvell", "Juvia Lockser", "Gajeel Redfox", "Levy McGarden",
    "Mirajane Strauss", "Elfman Strauss", "Lisanna Strauss",
    "Jellal Fernandes", "Sting Eucliffe", "Rogue Oro", "Zeref Alvarez",
    "Layla Heartfilia", "Igneel Dragneel",
    # Steins;Gate
    "Okabe Rintarou", "Makise Kurisu", "Shiina Mayuri", "Hashida Itaru",
    "Kiryuu Moeka", "Amane Suzuha", "Urushibara Ruka", "Farah Nae",
    # K-On!
    "Hirasawa Yui", "Akiyama Mio", "Tainaka Ritsu", "Kotobuki Tsumugi",
    "Nakano Azusa", "Manabe Nodoka", "Suzuki Jun", "Saito Sumire",
    # AOT
    "Eren Yeager", "Mikasa Ackerman", "Armin Arlert", "Levi Ackerman",
    "Erwin Smith", "Hange Zoe", "Jean Kirstein", "Connie Springer",
    "Sasha Blouse", "Historia Reiss", "Annie Leonhart",
    "Reiner Braun", "Bertolt Hoover", "Zeke Yeager", "Kenny Ackerman",
]

Kota = [
    "Tokyo", "Osaka", "Kyoto", "Yokohama", "Nagoya", "Sapporo",
    "Beika", "Uji", "Rokkenjima", "Magnolia",
    "Shibuya", "Shinjuku", "Akihabara", "Ikebukuro", "Hakone",
    "Sendai", "Kobe", "Fukuoka",
]

def generate_pelanggan(n):
    """Membangkitkan n record pelanggan dengan data acak."""
    data = []
    for i in range(1, n + 1):
        nama = random.choice(Nama_Pelanggan)
        email = f"{nama.lower().replace(' ', '.')}@gmail.com"
        tahun = random.randint(1980, 2009)
        bulan = random.randint(1, 12)
        hari = random.randint(1, 28)
        tgl_lahir = f"{tahun}-{bulan:02d}-{hari:02d}"
        total_belanja = random.randint(0, 50_000_000)
        kota = random.choice(Kota)

        data.append({
            "id": i,
            "nama": nama,
            "email": email,
            "tanggal_lahir": tgl_lahir,
            "bulan_lahir": bulan,
            "total_belanja": total_belanja,
            "kota": kota
        })
    return data

def simpan_csv(data, nama_file="data_customer.csv"):
    """Menyimpan data pelanggan ke file CSV."""
    with open(nama_file, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
    print(f"Data tersimpan di {nama_file}")

# Tahap 2: Implementasi Algoritma Awal (20%) =======
def cari_id_linear(data, target_id):
    """Pencarian berdasarkan ID"""
    for p in data:
        if p["id"] == target_id:
            return p
    return None

def cari_nama_linear(data, keyword):
    """Pencarian nama mengandung keyword (case insensitive)."""
    kw = keyword.lower()
    return [p for p in data if kw in p["nama"].lower()]

def top10_selection(data):
    """Mengambil 10 pelanggan dengan total_belanja tertinggi (selection parsial)."""
    hasil = []
    sisa = data.copy()
    for _ in range(10):
        if not sisa:
            break
        maks = max(sisa, key=lambda x: x["total_belanja"])
        hasil.append(maks)
        sisa.remove(maks)
    return hasil

def filter_bulan_linear(data, bulan):
    """Filter pelanggan berdasarkan bulan lahir"""
    return [p for p in data if p["bulan_lahir"] == bulan]

def statistik_kota(data):
    """Menghitung jumlah pelanggan per kota."""
    stat = {}
    for p in data:
        k = p["kota"]
        stat[k] = stat.get(k, 0) + 1
    return stat

# Tahap 5: Implementasi Perbaikan (15%)
def bangun_indeks(data):
    """Membangun dictionary, inverted index, dan struktur penunjang."""
    dict_id = {p["id"]: p for p in data}

    inverted = defaultdict(list)
    for p in data:
        for kata in set(p["nama"].lower().split()):
            inverted[kata].append(p["id"])

    dict_bulan = defaultdict(list)
    for p in data:
        dict_bulan[p["bulan_lahir"]].append(p)

    cnt_kota = Counter(p["kota"] for p in data)

    return dict_id, inverted, dict_bulan, cnt_kota

def cari_id_cepat(d, id_target):
    return d.get(id_target)

def cari_nama_cepat(inv, keyword):
    return inv.get(keyword.lower(), [])

def top10_heap(data):
    return heapq.nlargest(10, data, key=lambda x: x["total_belanja"])

def filter_bulan_cepat(dict_bln, bulan):
    return dict_bln.get(bulan, [])

def statistik_kota_cepat(cnt):
    return dict(cnt)

# Fungsi pengukuran waktu
def ukur(func, *args, _ulang=5):
    """Mengembalikan waktu rata-rata eksekusi fungsi (detik)."""
    total = 0.0
    for _ in range(_ulang):
        start = time.perf_counter()
        func(*args)
        total += time.perf_counter() - start
    return total / _ulang

def main():
    # Tahap 1
    print("\n- Membangkitkan 50.000 record pelanggan...")
    data_50k = generate_pelanggan(50000)
    simpan_csv(data_50k)
    print("Contoh 5 data pertama:")
    for p in data_50k[:5]:
        print("-" * 60)
        print(f"  {p['id']:>5}. {p['nama']:<25} | {p['kota']:<15} | "
              f"Rp{p['total_belanja']:>10,} | {p['tanggal_lahir']}")

    # Tahap 2 
    print("\n- Implementasi algoritma awal (linear search) siap digunakan.")

    # Tahap 3
    ukuran = [1000, 5000, 10000, 50000]
    hasil = {"cari_id": [], "cari_nama": [], "top10": [],
             "filter_bln": [], "stat_kota": []}

    print("\n- Tahap 3: Pengukuran kinerja fitur awal")
    print("-" * 70)
    print(f"{'n':>6} | {'Cari ID':>11} | {'Cari Nama':>11} | "
          f"{'Top 10':>11} | {'Filter Bulan':>13} | {'Stat Kota':>11}")
    print("-" * 70)

    for n in ukuran:
        data_n = data_50k[:n]
        t1 = ukur(cari_id_linear, data_n, data_n[-1]["id"])
        t2 = ukur(cari_nama_linear, data_n, "Edogawa")
        t3 = ukur(top10_selection, data_n, _ulang=2) if n <= 10000 \
             else ukur(top10_heap, data_50k, _ulang=1)
        t4 = ukur(filter_bulan_linear, data_n, 1)
        t5 = ukur(statistik_kota, data_n)

        hasil["cari_id"].append(t1)
        hasil["cari_nama"].append(t2)
        hasil["top10"].append(t3)
        hasil["filter_bln"].append(t4)
        hasil["stat_kota"].append(t5)

        print(f"{n:>6} | {t1:>11.6f} | {t2:>11.6f} | "
              f"{t3:>11.6f} | {t4:>13.6f} | {t5:>11.6f}")

    # --- Tahap 5: Perbaikan dan perbandingan ---
    print("\n>> Membangun struktur data optimal (dictionary, inverted index)...")
    dict_id, inv, dict_bln, cnt_kota = bangun_indeks(data_50k)

    print(">> Pengukuran setelah perbaikan (n=50.000):")
    t1_opt = ukur(cari_id_cepat, dict_id, 50000)
    t2_opt = ukur(cari_nama_cepat, inv, "Edogawa")
    t3_opt = ukur(top10_heap, data_50k)
    t4_opt = ukur(filter_bulan_cepat, dict_bln, 1)
    t5_opt = ukur(statistik_kota_cepat, cnt_kota)

    waktu_awal = [hasil["cari_id"][-1], hasil["cari_nama"][-1],
                  hasil["top10"][-1], hasil["filter_bln"][-1], hasil["stat_kota"][-1]]
    waktu_opt  = [t1_opt, t2_opt, t3_opt, t4_opt, t5_opt]
    label_fitur = ["Cari ID", "Cari Nama", "Top 10", "Filter Bulan", "Stat Kota"]

    print("\n- Perbandingan Sebelum vs Sesudah Perbaikan")
    print(f"{'Fitur':<18} | {'Sebelum (s)':>12} | {'Sesudah (s)':>12} | {'Percepatan':>10}")
    print("-" * 60)
    for fit, sblm, ssdh in zip(label_fitur, waktu_awal, waktu_opt):
        if ssdh > 0:
            print(f"{fit:<18} | {sblm:>12.6f} | {ssdh:>12.6f} | {sblm/ssdh:>10.1f}x")
        else:
            print(f"{fit:<18} | {sblm:>12.6f} | {ssdh:>12.6f} | {'∞':>10}")

    # --- Tahap 4: Analisis & Rekomendasi ---
    print("\n- ANALISIS & REKOMENDASI:")
    print("- Pencarian ID: O(n) -> O(1) menggunakan dictionary.")
    print("- Pencarian Nama: O(n) -> O(kata) dengan inverted index.")
    print("- Top 10: selection O(10n) -> heap O(n log 10), lebih ringan.")
    print("- Filter bulan: O(n) -> O(1) dengan dictionary of lists.")
    print("- Statistik kota: sudah O(n), Counter hanya penyederhanaan.")
    print("\nRekomendasi: gunakan dictionary untuk key lookup, heapq untuk top‑k,")
    print("dan pertimbangkan database berindeks jika data bertambah besar.")

    # --- Grafik ---
    plt.figure(figsize=(10, 5))
    for lbl, w in [("Cari ID", hasil["cari_id"]), ("Cari Nama", hasil["cari_nama"]),
                   ("Top 10", hasil["top10"]), ("Filter Bulan", hasil["filter_bln"]),
                   ("Stat Kota", hasil["stat_kota"])]:
        plt.plot(ukuran, w, marker='o', linewidth=2, label=lbl)
    plt.xlabel("Ukuran Data (n)")
    plt.ylabel("Waktu (detik)")
    plt.title("Pertumbuhan Waktu Fitur Sebelum Optimasi (Linear Search)")
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.savefig("sebelum_perbaikan.png")
    plt.show()

    plt.figure(figsize=(10, 5))
    x_pos = range(len(label_fitur))
    plt.bar([p - 0.2 for p in x_pos], waktu_awal, 0.4, label="Linear Search", color='salmon')
    plt.bar([p + 0.2 for p in x_pos], waktu_opt, 0.4, label="Optimasi", color='steelblue')
    plt.xticks(x_pos, label_fitur)
    plt.ylabel("Waktu (detik)")
    plt.title("Perbandingan Waktu Eksekusi (n=50.000)")
    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.savefig("perbandingan.png")
    plt.show()

    print("\nProyek Mini selesai. Grafik disimpan, data pelanggan tersedia di CSV.")

if __name__ == "__main__":
    main()