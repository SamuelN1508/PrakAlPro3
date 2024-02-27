try:
    # Masukan input
    bilangan = int(input("Masukan sebuah bilangan : "))
    # Percabangfan Ternary untuk mencari bilangan positif atau negatif
    hasil = "Nol" if bilangan <=1 else "Positif" if bilangan >= 0 else "Negatif"
    # Print jawabannya
    print(hasil)
except ValueError:
    # Jika bilangan bukan integer maka code dibawah akan dijalankan
    print("Masukan angka")