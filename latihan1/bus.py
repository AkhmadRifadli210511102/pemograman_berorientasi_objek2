class bus:
    def __init__(self, merk, warna, nomor_polisi):
        self.merk = merk
        self.warna = warna
        self.nomor_polisi = nomor_polisi

    def info(self):
        print(f'Mobil {self.merk} berwarna {self.warna} dengan nomor polisi {self.nomor_polisi}')

busA = bus('toyota', 'Putih hitam', 'E 1895 HG')
busA.info()