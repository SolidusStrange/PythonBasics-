quintil = int(input("Ingrese su quintil (1-5): "))
cond_laboral = input("Ingrese su condición laboral (empleado/desempleado): ").lower()
edad = int(input("Ingrese su edad: "))
bono = 0

if quintil==1 or quintil==2:
    if cond_laboral == "desempleado":
        bono = 10000 + 2000
    else:
        bono = 8000 + 2000
elif quintil==3:
    if cond_laboral == "desempleado":
        bono = 6000
    else:
        bono = 4000
else:
    bono = 1500
    
if edad>65:
    bono += 3000
    
print(f"El valor del subsidio de gas es: {bono}")


