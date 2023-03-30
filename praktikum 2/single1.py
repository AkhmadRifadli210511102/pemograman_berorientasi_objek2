class binatang:
    def _init_(self, nama, umur):
        self.nama = nama
        self.umur = umur
    def bergerak(self):
        print(self.nama, "berjalan")
class sapi(binatang):
    def _init_(self, nama, umur, warna_kulit):
        super()._init_(nama, umur)
        self.warna_kulit = warna_kulit
    def bersuara(self):
        print("mooo!")
sapiA = sapi("sapie", 2, "limosin")
sapiA.bergerak() # output: sapie berjalan
sapiA.bersuara() # output: Mooo!