
def jumlah_n(n):
    total = 0

    for i in range(1, n + 1):
        total += i

    return total


for n in [1, 5, 10, 100]:
    hasil_perulangan = jumlah_n(n)
    hasil_rumus = n * (n + 1) // 2

    print(f"n = {n}")
    print(f"Hasil perulangan = {hasil_perulangan}")
    print(f"Hasil rumus = {hasil_rumus}")
    print()
