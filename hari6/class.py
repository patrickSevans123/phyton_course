class Bangun_Datar:
    def __init__(self,alas,tinggi):
        self.alas = alas
        self.tinggi = tinggi
    def luas(self):
        luas_segitiga = self.alas * self.tinggi/2
        return f'luas:{luas_segitiga}'
segitiga = Bangun_Datar(10,5)
print(segitiga.luas())


