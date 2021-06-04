medida = float(input('Uma distância em metros:'))
cm = medida * 100
mm = medida * 1000
print('A medida {} é de {}cm e de milimetros é {}mm'.format(medida, cm, mm))
print('A medida {} é de {:.0f}cm que corresponde a {:.0f}mm'.format(medida, cm, mm))
