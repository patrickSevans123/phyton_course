import time

criminals = []

def add_criminal_to_list(name, age, crime):
    criminal_data = {
        "Fullname" : name,
        "Age" : age,
        "Crime" : crime
    }
    criminals.append(criminal_data)

tambah_berapa_orang = int(input("Mau tambahkan berapa pelaku krimina? "))
credit = 1
while credit <= tambah_berapa_orang1:
    nama_kriminal = input("Masukkan nama kriminal : ")
    
    credit = credit  + 1
    print()


my_password = ''
print("Tulis password : ")


while my_password != '123455':
    my_password = input ('Password? ')

print("Loading....")
time.sleep(1)

print()
print (len(criminals) , ' SELESAI')
print()

time.sleep(1)
print("DAFTAR KRIMINAL ")

