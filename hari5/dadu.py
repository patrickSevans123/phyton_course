import random


angka = random.randint(1,7)
credit = 0

while True:
    jawaban = int(input("Tebak angka dadu:"))

    if jawaban = angka:
        credit = credit + 1
    else:
        print("Anda salah")

    pilihan = input("Main lagi? y/n:")

    if pilihan == 'n':
        break