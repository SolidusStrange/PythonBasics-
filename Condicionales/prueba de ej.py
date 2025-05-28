quintil = int(input("ingrese el quintil al cual pertenece (1-5): "))
trabajo = input(" ingrese su condición laboral: \n1.desempleado \n2. empleado \n ")
edad = int(input("ingrese su edad: "))
bono = 0

if quintil <3:
    bono = (bono+2000)
if edad>=65:
    bono = (bono+3000)
if quintil <3 and trabajo == "1":
    bonofinal = (bono+10000)
elif quintil <3 and trabajo =="2":
    bonofinal = (bono+8000)
elif quintil ==3 and trabajo =="1":
    bonofinal = (bono+6000)
elif quintil ==3 and trabajo =="2":
    bonofinal = (bono+4000)
elif quintil >3 and trabajo =="2":
    bonofinal = (bono+1500)
print (f"El valor del subsidio de gas es ${bonofinal}")