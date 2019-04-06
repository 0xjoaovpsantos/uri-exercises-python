numeroDoFuncionario = (input())
horasTrabalhadas = int(input())
precoPorHora = float(input())

salario = horasTrabalhadas * precoPorHora
print("NUMBER = {}".format(numeroDoFuncionario))
print("SALARY = U$ {:.2f}".format(salario))