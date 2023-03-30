class Tumbuhan:
    def __init__(self, jenis, tinggi):
        self.jenis = jenis
        self.tinggi = tinggi

    def tumbuh(self):
        print(f"Tumbuhan {self.jenis} sedang tumbuh")

class TumbuhanPohon(Tumbuhan):
    def __init__(self, jenis, tinggi, jumlah_cabang):
        super().__init__(jenis, tinggi)
        self.jumlah_cabang = jumlah_cabang

    def tumbuh(self):
        super().tumbuh()
        print(f"Tumbuhan {self.jenis} memiliki {self.jumlah_cabang} cabang")

class TumbuhanBuah(Tumbuhan):
    def __init__(self, jenis, tinggi, jumlah_buah):
        super().__init__(jenis, tinggi)
        self.jumlah_buah = jumlah_buah

    def tumbuh(self):
        super().tumbuh()
        print(f"Tumbuhan {self.jenis} menghasilkan {self.jumlah_buah} buah")

class PohonMangga(TumbuhanBuah, TumbuhanPohon):
    def __init__(self, jenis, tinggi, jumlah_cabang, jumlah_buah):
        Tumbuhan.__init__(self, jenis, tinggi)
        TumbuhanPohon.__init__(self, jenis, tinggi, jumlah_cabang)
        TumbuhanBuah.__init__(self, jenis, tinggi, jumlah_buah)

    def tumbuh(self):
        super().tumbuh()
        print(f"Tumbuhan {self.jenis} menghasilkan buah yang berjumlah {self.jumlah_buah} dan memiliki {self.jumlah_cabang} cabang")

tumbuhan1 = PohonMangga("Mangga", 2.5, 8, 50)
tumbuhan1.tumbuh()