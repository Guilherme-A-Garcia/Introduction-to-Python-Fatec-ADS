qtd_h: float = 0
valor_hora: float = 0
perc_desc: float = 0
num_dep: float = 0
salario: float = 0
sal_liq: float = 0

qtd_h = float(input("Insira a quantidade de horas trabalhadas: "))
valor_hora = float(input("Insira o valor por hora: "))
perc_desc = float(input("Insira o percentual de desconto: "))
num_dep = float(input("Insira o número de dependentes: "))

salario = qtd_h * valor_hora
sal_liq = (salario - (perc_desc/100) * salario) + (100 * num_dep)

print("Salário líquido:", sal_liq)
