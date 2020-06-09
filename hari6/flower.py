class bunga:
    
    def __init__(self, nama_bunga, daun_bunga, harga_bunga):
        # Instance variable (atribut nya)
        self.nama_bunga = nama_bunga
        self.daun_bunga = daun_bunga
        self.harga_bunga = harga_bunga

    # 'Updating' methods
    # 1
    def update_nama(self, nama_baru):
        self.nama_bunga = nama_baru
        
    # 2 
    def update_daun(self, daun_baru):
        self.daun_bunga = daun_baru
    
    # 3 
    def update_harga(self, harga_baru):
        self.harga_bunga = harga_baru


    # 'Returning' methods
    # 1
    def return_nama(self):
        return self.nama_bunga

    # 2
    def return_daun(self):
        return self.daun_bunga

    # 3
    def return_harga(self):
        return self.bunga_price

    # Method buat print data
    def data_bunga(self):
        print(f"Bunga {self.nama_bunga} berkelopak {self.daun_bunga} seharga {self.harga_bunga}.")



kembang = bunga('Mawar', 5, 11.5)

# sebelum
kembang.data_bunga()

# Update namanya
kembang.update_nama('Kembang')
# Ganti jumlah daun
kembang.update_daun(7)
# Ganti harga
kembang.update_harga(20.5)

# setelah
kembang.data_bunga()


print(kembang.return_nama())

