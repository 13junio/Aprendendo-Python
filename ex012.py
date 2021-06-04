preço = float(input('Qual é o preço do produto? R$'))
preço = preço - (preço * 5 / 100)
print('O preço do produto com o desconto de 5% é de R$ {:.2f}'.format(preço))
#{:.2f}' não esquecer do ponto(.) flutuante.
