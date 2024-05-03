'''
Little Petya ama los regalos. Su mamá le compró dos cadenas del mismo tamaño para
su cumpleaños. Las cadenas consisten en letras latinas mayúsculas y minúsculas.
Ahora Petya quiere comparar esas dos cadenas lexicográficamente. No importa si las
letras están en mayúsculas o minúsculas. Ayuda a Petya a realizar la comparación.
'''

cadena1 = "abc"
cadena2 = "abd"

def comparar_cadenas_lexicograficas():
    if cadena1 < cadena2:
        #Si la primera cadena es menor que la segunda, retornar "-1".
        return "-1"
    elif cadena1 > cadena2:
        #Si la segunda cadena es menor que la primera, retornar "1".
        return "1"
    else:
        #Si las cadenas son iguales, retornar "0".
        return "0"

print(comparar_cadenas_lexicograficas())
