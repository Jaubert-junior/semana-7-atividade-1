def calcular_media_ajustada(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3

    if nota3 > 8:
        media += 1  

    if media > 10:
        media = 10  

    return media

#entrada de dados
nota1 = float(input().strip())
nota2 = float(input().strip())
nota3 = float(input().strip())

#processamento
media_final = calcular_media_ajustada(nota1, nota2, nota3)

#saída de dados
print(media_final) 