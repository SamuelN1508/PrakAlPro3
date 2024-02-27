try:
    suhu = int(input("Masukkan suhu tubuh: "))
    # Jika suhu melebihi 38 maka anda demam
    if suhu >= 38:
        print("Anda demam")
    # Jika suhu tidak melebihi 38 maka anda tidak demam
    else:
        print("Anda tidak demam")
        
except ValueError:
    # Jika bilangan bukan integer maka code dibawah akan dijalankan
    print("Masukan suhu yang benar")

