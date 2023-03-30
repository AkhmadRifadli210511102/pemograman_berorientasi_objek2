class Manusia:
    def _init_(self, nama, umur):
        self.nama = nama
        self.umur = umur
    def berbicara(self):
        print(f"{self.nama} sedang berbicara.")
class Dosen(Manusia):
    def _init_(self, nama, umur, nip):
        super()._init_(nama, umur)
        self.nip = nip
    def mengajar(self):
        print(f"{self.nama} dengan NIP {self.nip} sedang mengajar.")
dosenA = Dosen("Budi", 35, "123456")
dosenA.berbicara() # Output: Budi sedang berbicara.
dosenA.mengajar() # Output: Budi dengan NIP 123456 sedang mengajar.