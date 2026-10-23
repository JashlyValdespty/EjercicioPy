edad = int(input("¿Cual es tu edad?"))
nombre =str(input("¿Cual es tu nombre?"))
nota1 = float(input("Ingrese la nota1:"))
nota2 = float(input("Ingrese la nota2:"))
nota3 = float(input(" Ingrese la nota3:"))

resultado=(nota1+nota2+nota3)/3

if resultado >= 71: 
    print("Aprobaste")

else:
    print("Reprobado")


 