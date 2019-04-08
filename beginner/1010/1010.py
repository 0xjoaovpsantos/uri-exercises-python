codigoPeca1, quantidadePeca1, precoPeca1 = input().split()
codigoPeca2, quantidadePeca2, precoPeca2 = input().split()
totalPagar = (int(quantidadePeca1) * float(precoPeca1)) + (int(quantidadePeca2) * float(precoPeca2))
print("VALOR A PAGAR: R$ {:.2f}".format(totalPagar))
