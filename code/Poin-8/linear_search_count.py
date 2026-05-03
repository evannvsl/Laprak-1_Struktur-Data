def linear_search_count(arr, x):
    count = 0
    for i in range(len(arr)):
        count += 1
        if arr[i] == x:
            return i, count
    return -1, count

def main():
    data = [23, 45, 12, 67, 34, 89, 90]
    test_values = [67, 23, 78, 99]
    for val in test_values: 
        idx, steps = linear_search_count(data, val)
        if idx != -1:
            print (f"cari {val} ditemukan di indeks {idx} langkah: {steps}")
        else:
            print(f"cari {val} tidak ditemukan langkah: {steps}")
            
if __name__ == "__main__":    main()