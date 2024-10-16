import math as mt

notaa = float(input())
notab = float(input())

peso1 = 3.5
peso2 = 7.5

media_ponderada = (notaa*3.5+notab*7.5)/(3.5+7.5)
saida = "MEDIA ={media_ponderada:.5f}".format(media_ponderada)
print(saida)