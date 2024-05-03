cadena1 = "abc"
cadena2 = "abd"
def comparar_cadenas_lexicograficas():
    if cadena1 < cadena2:
        return "-1"
    elif cadena1 > cadena2:
        return "1"
    else:
        return "0"

print(comparar_cadenas_lexicograficas())
