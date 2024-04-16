

def mensagem(imc):
    if imc < 18.5:
        return ("Magreza")
    elif imc <= 24.9:
        return('Normal')
    elif imc <= 29.9:
        return('Sobrepeso')
    elif imc <= 39.9:
        return ('Obesidade Grau II')
    elif imc >= 40:
        return ("Obesidade Grave")