# Här skriver du din kod.

svar = input("Vad är mätarställningen idag? ")
z = float (svar)
svar = input("Vad var mätarställnigen för ett år sedan? ")
x = float (svar)
y = z - x
print("Antal körda mil:", y)

svar = input("Antal liter bensin? ")
c = float (svar)
v = c / y
print("Förbrukning per mil:", v)

