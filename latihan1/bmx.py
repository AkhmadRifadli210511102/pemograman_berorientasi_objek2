class bmx :
    def __init__(self, merk, warna):
        self.merk = merk
        self.warna = warna

    def info(self):
        print(f' Merk {self.merk} dengan warna {self.warna}')
    
bmxA = bmx('polygon razor','biru hitam')
bmxA.info()