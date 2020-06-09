# Semua hal di python = objek --> variabel, function, class --> menunjuk ke suatu address di memory komputer.
# Yang bukan objek --> statements (if, while, )

# Kalo function --> def nama_function():
# Kalo class --> class NamaKelas:
# CLASS --> blueprint --> dicopy sebanyak mungkin/ reproducible --> membuat suatu objek (instance)

# Syntax / format
# Best practice --> nama kelas --> huruf kapital
# Blueprint buat bikin objek 'orang'

    # Constructor function--> bakal dijalanin ketika lu bikin objek/instance (object instantiation)
    # Self --> dipake di setiap funct.
    # Function berada di dalam class --> methods
    # Self --> 'reserved' keyword --> selalu parameter pertama, dan gunanya untuk 'mengaitkan' suatu objek
    # Ke suatu class.


def function():
    print('hi')

class Orang:
    
    # Class attributes
    spesies = 'Homo Sapiens' 

    # Orang punya karakteristik --> nama, umur, sekolah
    def __init__(self, nama, umur, sekolah): # Double underscore
        # Instance / Objek attributes
        self.nama = nama # Attribut / ciri-ciri dari suatu objek
        self.umur = umur 
        self.sekolah = sekolah

    def data_diri(self):
        print("Hai nama saya {}, umur saya {} dan saya beresekolah di {}.".format(self.nama, self.umur, self.sekolah))

    def nama_orang(self):
        print(self.nama)

    
# Bikin objek --> menggunakan constructor

# Creating an object/ instantiation.
anthony = Orang('Anthony', 17, 'CC')

anthony.data_diri()

'''
anthony.nama_orang()
anthony.data_diri()
print()
print(anthony.nama)
print(anthony.umur)
print(anthony.sekolah)
'''


# radit = Orang('Radit', 18, 'PL')
# print(radit.nama)
# print(radit.umur)
# print(radit.sekolah)      
        