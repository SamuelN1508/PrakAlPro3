try:
    # Memasukan input a, b, c
    a = int(input("Masukan bilangan pertama : "))
    b = int(input("Masukan bilangan kedua : "))
    c = int(input("Masukan bilangan ketiga : "))
    # Percabangan untuk mencari bilangan terbesar
    if a > b and a > c:
        print("Terbesar: ", a)
    elif b > a and b > c:
        print("Terbesar: ", b)
    elif c > a and c > b:
        print("Terbesar: ", c)
except ValueError:
    # Jika bilangan bukan integer maka code dibawah akan dijalankan
    print("Masukan angka")