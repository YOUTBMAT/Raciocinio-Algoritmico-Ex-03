caminho = input("Qual caminho você escolhe? (esquerda/direita): ").lower()
if caminho == "esquerda":
    print("Você escolheu o caminho da esquerda e encontrou um rio.")
    decisao = input("Você deve decidir: atravessar ou voltar: ").lower()
    if decisao == "atravessar":
        print("Você atravessa o rio e chega a uma vila segura!")
    elif decisao == "voltar":
        print("Você volta e permanece perdido na floresta.")
    else:
        print("Decisão inválida. Você permanece perdido na floresta.")
elif caminho == "direita":
    print("Você escolheu o caminho da direita e encontrou uma montanha.")
    decisao = input("Você deve decidir: subir ou voltar: ").lower()
    if decisao == "subir":
        print("Você sobe a montanha e encontra um tesouro no topo!")
    elif decisao == "voltar":
        print("Você volta e permanece perdido na floresta.")
    else:
        print("Decisão inválida. Você permanece perdido na floresta.")
else:
    print("Caminho inválido. Você permanece perdido na floresta.")