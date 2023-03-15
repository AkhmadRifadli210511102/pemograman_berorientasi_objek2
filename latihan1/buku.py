class Buku :
    def __init__(self, Judul, Penulis, Penerbit):
        self.Judul = Judul
        self.penulis = Penulis 
        self.penerbit = Penerbit

    def info(self):
        print(f'''
        Judul Buku  : {self.Judul} 
        Penulis     : {self.penulis}
        Penerbit    : {self.penerbit}
        ''')

bukuC = Buku('lembaga keuangan islam', 'nurul huda', 'prenada media grup')
bukuC.info()