def verificar():
    if imc < 18.5:
        print("Você está muito magro")
    elif imc == 18.5 or imc < 24.9:
        print("Você está no peso normal")
    elif imc == 25.0 or imc < 29.9:
        print("Você está com sobrepeso")
    elif imc == 30.0 or imc < 39.9:
        print("Você está obeso")
    else:
        print("Você está com obesidade GRAVE")
  
def calculo(peso, altura):
    imc = peso/(altura **2)
    return imc
    
peso = float(input("Qual o seu peso?\n"))
altura = float(input("Qual a sua altura?\n"))

imc = calculo(peso, altura)
print("O seu imc é:", imc)

verificar()