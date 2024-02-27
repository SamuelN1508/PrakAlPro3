try:
    # Masukan Input bulan
    bulan = int(input("Masukkan bulan (1-12): "))
    # Jika input yang dimasukan 1, 3, 5, 7, 9, 11
    if bulan == 1 or bulan == 3 or bulan == 5 or bulan == 7 or bulan == 9 or bulan == 11:
        print("Jumlah hari: 31")
    # Jika input yang dimasukan 2
    elif bulan == 2:
        print("Jumlah hari: 28")
    # Jika input yang dimasukan 4, 6, 8, 10, 12
    elif bulan == 4 or bulan == 6 or bulan == 8 or bulan == 10 or bulan == 12:
        print("Jumlah hari: 30")
    # Jika input yang dimasukan tidak diantara 1-12
    elif bulan > 12 or bulan <= 0:
        print("Masukan angka 1-12")
except ValueError:
    # Jika bilangan bukan integer maka code dibawah akan dijalankan
    print("Masukan angka 1-12")