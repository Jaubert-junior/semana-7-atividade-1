#entrada de dados
caractere = (input().strip()).lower()
 
 #processamento e saída de dados
if caractere  in "bcdfghjklmnpqrstvwxyz": print("consoante")
elif caractere in "aeiou" :print("vogal")
elif caractere in "0123456789": print("número")
elif caractere != "consoante" and "vogal" and "número" : print("símbolo")