pilihan = input("Tulis yang ingin dihitung no1 untuk luas segitiga atau no2 luas lingkaran  : ")

if pilihan == '1':
    a = int(input('masukkan panjang segitiga: '))
    t = int(input('masukkan tinggi segitiga: '))
    hasil = a*t/2
elif pilihan == '2':
    r = int(input('masukkan jari-jari lingkaran'))
    phi = 3.14
    hasil = phi*r*r
else:
    hasil = print("Kamu salah memasukkan nomor")

print("Hasilnya adalah : {}".format(hasil))