x = float(input("Digite a coordenada x: "))
y = float(input("Digite a coordenada y: "))

if 0 < x < 10 and 0 < y < 10:
    print("Dentro do quadrado")
elif x == 0 or x == 10 or y == 0 or y == 10:
    print("Na borda do quadrado")
else:
    print("Fora do quadrado")