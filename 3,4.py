try:
    # Masukan Input sisi 1, 2 dan 3
    sisi1 = int(input("Masukan sisi 1 : "))
    sisi2 = int(input("Masukan sisi 2 : "))
    sisi3 = int(input("Masukan sisi 3 : "))
    # Jika sisi 1 sama dan 2 dan 3 menggunakan "and"
    if sisi1 == sisi2 and sisi2 == sisi3:
        print("Tiga sisi sama")
    # Jika hanya ada 1 yang sama menggunakan "or"
    elif sisi1 == sisi2 or sisi1 == sisi3 or sisi2 == sisi3:
        print("Dua sisi sama")
    # Jika dua kondisi diatas tidak dipenuhi semua
    else:
        print("Tidak ada yang sama")
    
except ValueError:
    # Jika bilangan bukan integer maka code dibawah akan dijalankan
    print("Masukan input integer")