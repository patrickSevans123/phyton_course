pilihan = input("Tulis yang ingin dihitung no1 untuk volume balok atau no2 volume bola  : ")

if pilihan == '1':
    p = int(input('masukkan panjang balok: '))
    l = int(input('masukkan lebar balok: '))
    t = int(input('masukkan tinggi balok: '))
    hasil = p*l*t  
elif pilihan == '2':
    r = int(input('masukkan jari-jari bola'))
    phi = 3.14
    hasil = 4/3*phi*r*r*r
else:
    hasil = print("Kamu salah memasukkan nomor")

print("Hasilnya adalah : {}".format(hasil))