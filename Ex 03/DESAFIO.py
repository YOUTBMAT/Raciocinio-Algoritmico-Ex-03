lado1 = int(input("Digite o valor do lado 1: "))
lado2 = int(input("Digite o valor do lado 2: "))
lado3 = int(input("Digite o valor do lado 3: "))

if lado1+lado2>lado3 and lado1+lado3>lado2 and lado2+lado3>lado1:
    tri=True
else:
    tri=False

if tri!=True:
    print("Essas medidas não formam um triângulo")

if tri==True:
    if lado1 == lado2 == lado3:
        equilatero = True
        if equilatero == True:
            print("O triângulo é equilátero")
    elif lado1==lado2 or lado1==lado3 or lado2==lado3:
        isociles = True
        if isociles==True:
            print("O triângulo é isósceles")
    elif  lado1!=lado2!=lado3:
        escaleno=True
        if escaleno==True:
            print("O triângulo é escaleno")

if tri==True:
    if (lado1*lado1)+(lado2*lado2)==lado3**2 or (lado1*lado1)+(lado3*lado3)==lado2**2 or (lado3*lado3)+(lado2*lado2)==lado1**2:
        print("O triângulo é retângulo")


