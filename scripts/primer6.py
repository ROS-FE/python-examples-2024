
class clovek:
    def __init__(self, ime, starost):
        self.ime = ime
        self.starost = starost

    def rojstniDan(self):
        self.starost += 1

class student(clovek):
    fakulteta = "ULFE" #spremenljivka, ki je skupna vsem instancam
    def __init__(self, vpSt, ime, starost):
        super().__init__(ime, starost)
        self.vpisnaSt = vpSt #spremenljivka, vezana na instanco

    def spremeniVpisnoSt(self, novaVpSt):
        self.vpisnaSt = novaVpSt


studentJanez = student(739, "Janez", 33)
studentMarko = student(672, "Marko", 22)

print(studentJanez.vpisnaSt)
studentJanez.vpisnaSt = 924
studentMarko.spremeniVpisnoSt(666)
studentMarko.rojstniDan()
print(studentMarko.starost)

studentMarko.fakulteta = "ULFS"

print(studentJanez.fakulteta)