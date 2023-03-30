class Mahasiswa:
    def _init_(self, nama, nim):
        self.nama = nama
        self.nim = nim
    def belajar(self):
        print(self.nama, "sedang belajar")
class Pekerja:
    def _init_(self, nama, pekerjaan):
        self.nama = nama
        self.pekerjaan = pekerjaan
    def bekerja(self):
        print(self.nama, "sedang bekerja")
class MahasiswaPekerja(Mahasiswa, Pekerja):
    def _init_(self, nama, nim, pekerjaan):
        Mahasiswa._init_(self, nama, nim)
        Pekerja._init_(self, nama, pekerjaan)
    def bersosialisasi(self):
        print(self.nama, "sedang bersosialisasi")
mhs_pekerja = MahasiswaPekerja("Rahma", "190001", "Programmer")
mhs_pekerja.belajar() # output: Rahma sedang belajar
mhs_pekerja.bekerja() # output: Rahma sedang bekerja
mhs_pekerja.bersosialisasi() # output: Rahma sedang bersosialisasi