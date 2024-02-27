try:
    # Masukan input
    bilangan = int(input("Masukan suatu bilangan:"))
    # Jika bilangan melebihi 0 maka itu bilangan positif
    if bilangan > 0:
        print("Positif")
    # Jika bilangan kurang dari 0 maka itu bilangan negatif
    elif bilangan < 0:
        print("Negatif")
    # Jika bilangan sama dengan 
    elif bilangan == 0:
        print("Nol")
except ValueError:
    # Jika bilangan bukan integer maka code dibawah akan dijalankan
    print("Masukan angka")
    
