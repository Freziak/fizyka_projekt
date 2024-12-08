# Program liczacy napiecie skuteczne i napiecie maksymalne

pole1 = float(input("Podaj wymiar x: "))
pole2 = float(input("Podaj wymiar y: "))
S = (pole1 * pole2) / 10000 #pole
N = int(input("Podaj ilosc zwoji: ")) #zwoje
F = float(input("Podaj czestotliwosc w Hz: "))
B = float(input("Podaj pole magnetyczne: "))
pierwiastek = 1.4142
pi = 3.1415

omega = 2 * pi * F

Umax = N*B*S*omega
print(round(Umax,2))

Usk = Umax / pierwiastek
print(round(Usk, 2))