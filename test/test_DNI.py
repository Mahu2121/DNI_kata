

numero_casos = 15
letrasNoPermitidas = ["I", "Ñ", "O", "U"]

for i in range(1, numero_casos + 1):
    caso = ""
    for j in range(1, 9):
        caracterAscii = random.randrange(48, 57 + 1, 1)
        caso = caso + chr(caracterAscii)
    caso = caso + letrasNoPermitidas[random.randrange(0, 3 + 1, 1)]
    casosTest = casosTest + [caso]

print("\n## CASOS TEST ##\n")

print(casosTest)
