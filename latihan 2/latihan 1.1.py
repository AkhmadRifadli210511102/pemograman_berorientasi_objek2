class Hewan:
    def _init_(self, nama, umur):
        self.nama = nama
        self.umur = umur
    def bergerak(self):
        print(self.nama, "bergerak")
class Kucing(Hewan):
    def _init_(self, nama, umur, jenis_bulu):
        super()._init_(nama, umur)
        self.jenis_bulu = jenis_bulu
    def bersuara(self):
        print("Meow!")
kucingA = Kucing("Kitty", 2, "Persia")
kucingA.bergerak() # output: Kitty bergerak
kucingA.bersuara() # output: Meow!