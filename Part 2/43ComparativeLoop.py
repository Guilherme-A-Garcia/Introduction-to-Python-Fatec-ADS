ana_altura: float
maria_altura: float
anos: int

anos = 0
ana_altura = 1.1
maria_altura = 1.5

while ana_altura < maria_altura:
    ana_altura += 0.03
    maria_altura += 0.02
    anos += 1
    
print(anos)
