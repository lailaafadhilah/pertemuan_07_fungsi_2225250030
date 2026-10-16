
def luas_persegi_panjang(p, l):
    return p * l


def luas_segitiga(a, t):
    return 0.5 * a * t


def jumlah_n(n):
    if not isinstance(n, int) or isinstance(n, bool) or n < 0:
        raise ValueError("n harus bilangan bulat nonnegatif")

    total = 0

    for i in range(1, n + 1):
        total += i

    return total


def faktorial(n):
    if not isinstance(n, int) or isinstance(n, bool) or n < 0:
        raise ValueError("n harus bilangan bulat nonnegatif")

    hasil = 1

    for i in range(2, n + 1):
        hasil *= i

    return hasil


def tampilkan_menu():
    print("\n=== UTILITAS MATEMATIKA ===")
    print("1. Luas persegi panjang")
    print("2. Luas segitiga")
    print("3. Jumlah 1 sampai n")
    print("4. Faktorial")
    print("5. Keluar")


def input_bilangan(pesan):
    while True:
        try:
            nilai = float(input(pesan))

            if nilai < 0:
                print("Nilai tidak boleh negatif.")
            else:
                return nilai

        except ValueError:
            print("Masukkan angka yang valid.")


def input_n(pesan):
    while True:
        try:
            n = int(input(pesan))

            if n < 0:
                print("n harus nonnegatif.")
            else:
                return n

        except ValueError:
            print("n harus berupa bilangan bulat nonnegatif.")


def main():
    while True:
        tampilkan_menu()
        pilihan = input("Pilihan: ").strip()

        if pilihan == "1":
            p = input_bilangan("Panjang: ")
            l = input_bilangan("Lebar: ")
            print("Luas =", luas_persegi_panjang(p, l))

        elif pilihan == "2":
            a = input_bilangan("Alas: ")
            t = input_bilangan("Tinggi: ")
            print("Luas =", luas_segitiga(a, t))

        elif pilihan == "3":
            n = input_n("Masukkan n: ")
            print("Jumlah =", jumlah_n(n))

        elif pilihan == "4":
            n = input_n("Masukkan n: ")
            print("Faktorial =", faktorial(n))

        elif pilihan == "5":
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid.")


if __name__ == "__main__":
    main()
