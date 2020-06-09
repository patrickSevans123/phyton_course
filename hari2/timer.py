detik = int(input("Masukkan berapa detik : "))
menit = int(input("Masukkan berapa menit : "))
jam = int(input("Masukkan berapa jam : "))
waktu = detik + menit*60 + jam*3600
for x in range(waktu+1)
    print(waktu-x)
time.sleep(1)
print("Waktu Habis")