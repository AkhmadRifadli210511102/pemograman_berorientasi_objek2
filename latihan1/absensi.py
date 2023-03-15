class absensi:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim

    def info(self):
        print(f'Nama\t: {self.nama} \nNim\t: {self.nim}')

absensiA = absensi('Akmad Rifadli', '210511102')
absensiA.info()