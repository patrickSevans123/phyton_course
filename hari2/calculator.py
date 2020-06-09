
operasi = input("Masukkan operasi : ")
angka_1 = int(input("Masukkan angka 2 : "))
angka_2 = int(input("Masukkan angka 1 : "))
if operasi == '+':
    hasil = angka_1 + angka_2
elif operasi == '-':
    hasil = angka_1 - angka_2
elif operasi == '*':
    hasil = angka_1 * angka_2
elif operasi == '/':
    if angka_2 == 0:
        hasil = "Gak bisa dibagi nol"
    else:
        hasil = angka_1 / angka_2
else:
    hasil = "Anda salah memasukkan operasi."

print("Hasilnya adalah : {}".format(hasil))