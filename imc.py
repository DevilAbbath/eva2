weight = float(input("Ingrese su Peso en Kg: "))
height = float(input("Ingrese su altura en cm: "))

mheight = height / 100
imc = weight/(mheight ** 2)

clasificacion = ""

if imc < 8.5:
    clasificacion = "Bajo Peso"

elif 18.5 < imc < 25:
    clasificacion = "Peso Adecuado"

elif 25 <= imc < 30:
    clasificacion = "Sobre Peso"

elif 30 <= imc < 35:
    clasificacion = "Obesidad 1"

elif 35 <= imc < 40:
    clasificacion = "Obesidad 2"

elif 40 <= imc:
    clasificacion = "Obesidad 3"

else:
    clasificacion = "Indeterminada"


print (f'Su IMC es de {imc:.2f}')
print (f'La clasificacion OMS es {clasificacion}')