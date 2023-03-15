class Celcius:
    @staticmethod
    def Fahrenhait(celcius):
        return (celcius * 9/5) + 32
    
    @staticmethod
    def Kelvin(celcius):
        return celcius + 273.15
    
    @staticmethod
    def Reamur(celcius):
        return celcius * 4/5
    
brpcelcius = 45
fahrenheit = Celcius.Fahrenhait(brpcelcius)
kelvin = Celcius.Kelvin(brpcelcius)
reamur = Celcius.Reamur(brpcelcius)

print(f'''
45 Celcius ke\t:
Fahrenheit\t: {fahrenheit}
Kelvin\t\t: {kelvin}
Reamur\t\t: {reamur}
''')
    
