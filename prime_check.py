import math

def is_prime(n):
    if n <= 1:
        return False, 0
    if n == 2:
        return True, 0
    if n % 2 == 0:
        return False, 1
    iter_count = 0
    i = 3
     
    while i * i <= n:
        iter_count += 1
        if n % i == 0:
            return False, iter_count
        i += 2
    return True, iter_count

def main():
    test_numbers = [2, 3, 17, 19, 23, 97, 100, 101, 997, 999, 1000]
    print("=" * 60)
    print("Pengujian Bilangan Prima")
    print("=" * 60)

    print(f"{'n':<10} {'Prima':<8} {'Iterasi':<10} {'√n':<10}")
    print("-" * 60)
    
    for n in test_numbers:
        prima, iterasi = is_prime(n)
        akar = int(math.sqrt(n))
        status = "Ya" if prima else "Tidak"
        print(f"{n:<10} {status:<8} {iterasi:<10} {akar:<10}")
        
if __name__ == "__main__": 
    main()