class Lingkaran:
    def __init__(self, jari_jari):
        self.jari_jari = jari_jari

    def Luas(self):
        return (22/7) * (self.jari_jari ** 2) 
    
    def Keliling(self):
        return 2 * (22/7) * self.jari_jari
    
LingkaranB = Lingkaran(14)
print(f'Luas Lingkaran\t\t= {LingkaranB.Luas()}\nKeliling Lingkaran\t= {LingkaranB.Keliling()}')